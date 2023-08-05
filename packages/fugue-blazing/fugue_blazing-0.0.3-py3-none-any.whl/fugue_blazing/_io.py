import os
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import cudf
import pandas as pd
from fugue_blazing.dataframe import CudaDataFrame
from triad.collections.dict import ParamDict
from triad.collections.fs import FileSystem
from triad.collections.schema import Schema
from triad.exceptions import InvalidOperationError
from triad.utils.assertion import assert_or_throw

from fugue import PandasDataFrame
from fugue._utils.io import FileParser, _get_single_files
from fugue._utils.io import _load_avro as _pd_load_avro
from fugue._utils.io import _save_avro as _pd_save_avro


def load_df(
    uri: Union[str, List[str]],
    format_hint: Optional[str] = None,
    columns: Any = None,
    fs: Optional[FileSystem] = None,
    **kwargs: Any,
) -> CudaDataFrame:
    if isinstance(uri, str):
        fp = [FileParser(uri, format_hint)]
    else:
        fp = [FileParser(u, format_hint) for u in uri]
    dfs: List[pd.DataFrame] = []
    schema: Any = None
    for f in _get_single_files(fp, fs):
        df, schema = _FORMAT_LOAD[f.file_format](f.assert_no_glob(), columns, **kwargs)
        dfs.append(df)
    return CudaDataFrame(cudf.concat(dfs), schema)


def save_df(
    df: CudaDataFrame,
    uri: str,
    format_hint: Optional[str] = None,
    mode: str = "overwrite",
    fs: Optional[FileSystem] = None,
    **kwargs: Any,
) -> None:
    assert_or_throw(
        mode in ["overwrite", "error"], NotImplementedError(f"{mode} is not supported")
    )
    p = FileParser(uri, format_hint).assert_no_glob()
    if fs is None:
        fs = FileSystem()
    if fs.exists(uri):
        assert_or_throw(mode == "overwrite", FileExistsError(uri))
        try:
            fs.remove(uri)
        except Exception:
            try:
                fs.removetree(uri)
            except Exception:  # pragma: no cover
                pass
    _FORMAT_SAVE[p.file_format](df, p, **kwargs)


def _save_parquet(df: CudaDataFrame, p: FileParser, **kwargs: Any) -> None:
    df.native.to_parquet(p.uri, index=False, **kwargs)


def _safe_load_parquet(path: str, **kwargs: Any) -> cudf.DataFrame:
    fs = FileSystem()
    if fs.isfile(path):
        return cudf.read_parquet(path, **kwargs)
    else:
        dfs: List[cudf.DataFrame] = []
        for fp in FileSystem().listdir(path):
            if fp.endswith(".parquet"):
                dfs.append(cudf.read_parquet(os.path.join(path, fp), **kwargs))
        return cudf.concat(dfs)


def _load_parquet(
    p: FileParser, columns: Any = None, **kwargs: Any
) -> Tuple[cudf.DataFrame, Any]:
    if columns is None:
        pdf = _safe_load_parquet(p.uri, **kwargs)
        return pdf, None
    if isinstance(columns, list):  # column names
        pdf = _safe_load_parquet(p.uri, columns=columns, **kwargs)
        return pdf, None
    schema = Schema(columns)
    pdf = _safe_load_parquet(p.uri, columns=schema.names, **kwargs)
    return pdf, schema


def _save_csv(df: CudaDataFrame, p: FileParser, **kwargs: Any) -> None:
    df.native.to_csv(p.uri, **{"index": False, "header": False, **kwargs})


def _safe_load_csv(path: str, **kwargs: Any) -> cudf.DataFrame:
    fs = FileSystem()
    if fs.isfile(path):
        return cudf.read_csv(path, **kwargs)
    else:
        dfs: List[cudf.DataFrame] = []
        for fp in FileSystem().listdir(path):
            if fp.endswith(".csv"):
                dfs.append(cudf.read_csv(os.path.join(path, fp), **kwargs))
        return cudf.concat(dfs)


def _load_csv(
    p: FileParser, columns: Any = None, **kwargs: Any
) -> Tuple[cudf.DataFrame, Any]:
    kw = ParamDict(kwargs)
    infer_schema = kw.get("infer_schema", False)
    if not infer_schema:
        kw["dtype"] = object
    if "infer_schema" in kw:
        del kw["infer_schema"]
    header: Any = False
    if "header" in kw:
        header = kw["header"]
        del kw["header"]
    if str(header) in ["True", "0"]:
        pdf = _safe_load_csv(p.uri, **{"index_col": False, "header": 0, **kw})
        if columns is None:
            return pdf, None
        if isinstance(columns, list):  # column names
            return pdf[columns], None
        schema = Schema(columns)
        return pdf[schema.names], schema
    if header is None or str(header) == "False":
        if columns is None:
            raise InvalidOperationError("columns must be set if without header")
        if isinstance(columns, list):  # column names
            pdf = _safe_load_csv(
                p.uri, **{"index_col": False, "header": None, "names": columns, **kw}
            )
            return pdf, None
        schema = Schema(columns)
        pdf = _safe_load_csv(
            p.uri, **{"index_col": False, "header": None, "names": schema.names, **kw}
        )
        return pdf, schema
    else:
        raise NotImplementedError(f"{header} is not supported")


def _save_json(df: CudaDataFrame, p: FileParser, **kwargs: Any) -> None:
    df.native.to_json(p.uri, **{"orient": "records", "lines": True, **kwargs})


def _safe_load_json(path: str, **kwargs: Any) -> cudf.DataFrame:
    kw = {"orient": "records", "lines": True, **kwargs}
    fs = FileSystem()
    if fs.isfile(path):
        return cudf.read_json(path, **kw)
    else:
        dfs: List[cudf.DataFrame] = []
        for fp in FileSystem().listdir(path):
            if fp.endswith(".json"):
                dfs.append(cudf.read_json(os.path.join(path, fp), **kw))
        return cudf.concat(dfs)


def _load_json(
    p: FileParser, columns: Any = None, **kwargs: Any
) -> Tuple[cudf.DataFrame, Any]:
    pdf = _safe_load_json(p.uri, **kwargs).reset_index(drop=True)
    if columns is None:
        return pdf, None
    if isinstance(columns, list):  # column names
        return pdf[columns], None
    schema = Schema(columns)
    return pdf[schema.names], schema


def _save_avro(df: CudaDataFrame, p: FileParser, **kwargs: Any) -> None:
    df.native.to_json(p.uri, **kwargs)
    _pd_save_avro(
        PandasDataFrame(df.as_pandas(), schema=df.schema, pandas_df_wrapper=True),
        p,
        **kwargs,
    )


def _load_avro(
    p: FileParser, columns: Any = None, **kwargs: Any
) -> Tuple[cudf.DataFrame, Any]:
    pdf, schema = _pd_load_avro(p, columns=columns, **kwargs)
    return cudf.DataFrame.from_pandas(pdf), schema


_FORMAT_LOAD: Dict[str, Callable[..., Tuple[pd.DataFrame, Any]]] = {
    "csv": _load_csv,
    "parquet": _load_parquet,
    "json": _load_json,
    "avro": _load_avro,
}

_FORMAT_SAVE: Dict[str, Callable] = {
    "csv": _save_csv,
    "parquet": _save_parquet,
    "json": _save_json,
    "avro": _save_avro,
}

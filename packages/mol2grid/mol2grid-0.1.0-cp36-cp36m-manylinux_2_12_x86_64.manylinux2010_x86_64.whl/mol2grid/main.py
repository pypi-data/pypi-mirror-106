import os
import numpy
from typing import Optional, Tuple

all = ["lig2grid", "rec2grid", "pair2grid"]


def cli():
    return


def lig2grid(
    ligand: str,
    receptor: str,
    padding: float,
    step: float = 0.6,
    file: Optional[str] = None,
    vdw: Optional[str] = None,
    catalog: Optional[str] = None,
    nthreads: int = os.cpu_count() - 1,
    verbose: bool = False,
) -> numpy.ndarray:
    from .utils import read_vdw, read_catalog, read_mol, define_grid
    from _mol2grid import fill, export

    # If user defined a custom van der Waals file, load it
    if vdw is not None:
        vdw = read_vdw(vdw)
    # Else, load default file
    else:
        vdw = read_vdw()

    # If user defined a custom catlog file, load it
    if catalog is not None:
        catalog = read_catalog(catalog)
    # Else, load default file
    else:
        catalog = read_catalog()

    # Load ligand and receptor coordinates, radii and barcodes
    rec = read_mol(receptor, vdw, catalog)
    xyzrc = read_mol(ligand, vdw, catalog)

    # Define grid
    origin, sincos, nx, ny, nz = define_grid(rec, padding, step)

    # Insert ligand in grid
    lig = fill(
        nx * ny * nz, nx, ny, nz, xyzrc, origin, sincos, step, nthreads, verbose
    ).reshape(nx, ny, nz)

    # If user defined a file, export cavities to defined file
    if file is not None:
        export(file, lig, origin, sincos, step, nthreads)

    return lig


def rec2grid(
    receptor: str,
    padding: float,
    step: float = 0.6,
    file: Optional[str] = None,
    vdw: Optional[str] = None,
    catalog: Optional[str] = None,
    nthreads: int = os.cpu_count() - 1,
    verbose: bool = False,
) -> numpy.ndarray:
    from .utils import read_vdw, read_catalog, read_mol, define_grid
    from _mol2grid import fill, export

    # If user defined a custom van der Waals file, load it
    if vdw is not None:
        vdw = read_vdw(vdw)
    # Else, load default file
    else:
        vdw = read_vdw()

    # If user defined a custom catlog file, load it
    if catalog is not None:
        catalog = read_catalog(catalog)
    # Else, load default file
    else:
        catalog = read_catalog()

    # Load receptor coordinates, radii and barcodes
    xyzrc = read_mol(receptor, vdw, catalog)

    # Define grid
    origin, sincos, nx, ny, nz = define_grid(xyzrc, padding, step)

    # Insert ligand in grid
    rec = fill(
        nx * ny * nz, nx, ny, nz, xyzrc, origin, sincos, step, nthreads, verbose
    ).reshape(nx, ny, nz)

    # If user defined a file, export cavities to defined file
    if file is not None:
        export(file, rec, origin, sincos, step, nthreads)

    return rec


def pair2grid(
    ligand: str,
    receptor: str,
    padding: float,
    step: float = 0.6,
    ligfile: Optional[str] = None,
    recfile: Optional[str] = None,
    vdw: Optional[str] = None,
    catalog: Optional[str] = None,
    nthreads: int = os.cpu_count() - 1,
    verbose: bool = False,
) -> Tuple[numpy.ndarray, numpy.ndarray]:
    from .utils import read_vdw, read_catalog, read_mol, define_grid
    from _mol2grid import fill, export

    # If user defined a custom van der Waals file, load it
    if vdw is not None:
        vdw = read_vdw(vdw)
    # Else, load default file
    else:
        vdw = read_vdw()

    # If user defined a custom catlog file, load it
    if catalog is not None:
        catalog = read_catalog(catalog)
    # Else, load default file
    else:
        catalog = read_catalog()

    # Define grid
    rec = read_mol(receptor, vdw, catalog)
    origin, sincos, nx, ny, nz = define_grid(rec, padding, step)

    # Load ligand coordinates, radii and barcodes
    xyzrc = read_mol(ligand, vdw, catalog)

    # Insert ligand in grid
    lig = fill(
        nx * ny * nz, nx, ny, nz, xyzrc, origin, sincos, step, nthreads, verbose
    ).reshape(nx, ny, nz)

    # If user defined a file, export cavities to defined file
    if ligfile is not None:
        export(ligfile, lig, origin, sincos, step, nthreads)

    # Load receptor coordinates, radii and barcodes
    xyzrc = read_mol(receptor, vdw, catalog)

    # Insert ligand in grid
    rec = fill(
        nx * ny * nz, nx, ny, nz, xyzrc, origin, sincos, step, nthreads, verbose
    ).reshape(nx, ny, nz)

    # If user defined a file, export cavities to defined file
    if recfile is not None:
        export(recfile, rec, origin, sincos, step, nthreads)

    return lig, rec

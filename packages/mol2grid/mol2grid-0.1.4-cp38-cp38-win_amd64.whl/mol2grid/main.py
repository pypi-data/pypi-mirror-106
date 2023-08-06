import os
import numpy
from typing import Optional, Tuple

__all__ = ["lig2grid", "rec2grid", "pair2grid"]


def lig2grid(
    ligand: str,
    receptor: str,
    padding: float,
    step: float = 0.6,
    file: Optional[str] = None,
    vdw: Optional[str] = None,
    catalog: Optional[str] = None,
    ignore_h: bool = True,
    nthreads: int = os.cpu_count() - 1,
    verbose: bool = False,
) -> numpy.ndarray:
    f"""Inserts a target ligand to a 3D grid, created based on the receptor, a
    padding and a grid spacing (step)

    Parameters
    ----------
    ligand : str
        A path to a PDB-formatted file of a target ligand
    receptor : str
        A path to a PDB-formatted file of a target receptor
    padding : float
        A length to be added in each direction of the 3D grid
    step : float, optional
        Grid spacing (A), by default 0.6
    file : Optional[str], optional
        A path to a PDB-formatted file to write the grid points where atoms
        lay on and the barcodes are mapped on the B-values, by default None
    vdw : Optional[str], optional
        A path to a custom van der Waals radii file, by default None
    catalog : Optional[str], optional
        A path to a custom catalog file, by default None
    ignore_h : bool, optional
        Whether to ignore hydrogen atoms, by default True
    nthreads : int, optional
        Number of threads, by default {os.cpu_count()-1}
    verbose : bool, optional
        Whether to print extra information to standard output, by default False

    Returns
    -------
    numpy.ndarray
        A numpy.ndarray with grid points corresponding to the atom barcodes of
        the ligand

    Note
    ----
    Greater barcodes have priority in the 3D grid when atoms overlap
    """
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
    rec = read_mol(receptor, vdw, catalog, ignore_h)
    xyzrc = read_mol(ligand, vdw, catalog, ignore_h)

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
    ignore_h: bool = True,
    nthreads: int = os.cpu_count() - 1,
    verbose: bool = False,
) -> numpy.ndarray:
    """Inserts a target receptor to a 3D grid, created based on the receptor, a
    padding and a grid spacing (step)

    Parameters
    ----------
    receptor : str
        A path to a PDB-formatted file of a target receptor
    padding : float
        A length to be added in each direction of the 3D grid
    step : float, optional
        Grid spacing (A), by default 0.6
    file : Optional[str], optional
        A path to a PDB-formatted file to write the grid points where atoms
        lay on and the barcodes are mapped on the B-values, by default None
    vdw : Optional[str], optional
        A path to a custom van der Waals radii file, by default None
    catalog : Optional[str], optional
        A path to a custom catalog file, by default None
    ignore_h : bool, optional
        Whether to ignore hydrogen atoms, by default True
    nthreads : int, optional
        Number of threads, by default {os.cpu_count()-1}
    verbose : bool, optional
        Whether to print extra information to standard output, by default False

    Returns
    -------
    numpy.ndarray
        A numpy.ndarray with grid points corresponding to the atom barcodes of
        the receptor

    Note
    ----
    Greater barcodes have priority in the 3D grid when atoms overlap
    """
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
    xyzrc = read_mol(receptor, vdw, catalog, ignore_h)

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
    ignore_h: bool = True,
    nthreads: int = os.cpu_count() - 1,
    verbose: bool = False,
) -> Tuple[numpy.ndarray, numpy.ndarray]:
    """Inserts a target receptor to a 3D grid, created based on the receptor, a
    padding and a grid spacing (step)

    Parameters
    ----------
    ligand : str
        A path to a PDB-formatted file of a target ligand
    receptor : str
        A path to a PDB-formatted file of a target receptor
    padding : float
        A length to be added in each direction of the 3D grid
    step : float, optional
        Grid spacing (A), by default 0.6
    ligfile : Optional[str], optional
        A path to a PDB-formatted file to write the grid points where atoms
        of the ligand lay on and the barcodes are mapped on the B-values,
        by default None
    recfile : Optional[str], optional
        A path to a PDB-formatted file to write the grid points where atoms
        of the receptor lay on and the barcodes are mapped on the B-values,
        by default None
    vdw : Optional[str], optional
        A path to a custom van der Waals radii file, by default None
    catalog : Optional[str], optional
        A path to a custom catalog file, by default None
    ignore_h : bool, optional
        Whether to ignore hydrogen atoms, by default True
    nthreads : int, optional
        Number of threads, by default {os.cpu_count()-1}
    verbose : bool, optional
        Whether to print extra information to standard output, by default False

    Returns
    -------
    Tuple[numpy.ndarray, numpy.ndarray]
        A tuple with numpy.ndarrays with grid points corresponding to the
        atom barcodes of the ligand and the receptor

    Note
    ----
    Greater barcodes have priority in the 3D grid when atoms overlap
    """
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
    rec = read_mol(receptor, vdw, catalog, ignore_h)
    origin, sincos, nx, ny, nz = define_grid(rec, padding, step)

    # Load ligand coordinates, radii and barcodes
    xyzrc = read_mol(ligand, vdw, catalog, ignore_h)

    # Insert ligand in grid
    lig = fill(
        nx * ny * nz, nx, ny, nz, xyzrc, origin, sincos, step, nthreads, verbose
    ).reshape(nx, ny, nz)

    # If user defined a file, export cavities to defined file
    if ligfile is not None:
        export(ligfile, lig, origin, sincos, step, nthreads)

    # Load receptor coordinates, radii and barcodes
    xyzrc = read_mol(receptor, vdw, catalog, ignore_h)

    # Insert ligand in grid
    rec = fill(
        nx * ny * nz, nx, ny, nz, xyzrc, origin, sincos, step, nthreads, verbose
    ).reshape(nx, ny, nz)

    # If user defined a file, export cavities to defined file
    if recfile is not None:
        export(recfile, rec, origin, sincos, step, nthreads)

    return lig, rec


def cli_l2g():
    """
    lig2grid Command Line Interface (CLI)

    Parameters
    ----------
        None

    Returns
    -------
        None

    Example
    -------
    Usage: lig2grid [-h] [-v] [--version] [-p <float>] [-s <float>] \
        [--ignore_h] [-o <str>] [--nthreads <int>] <ligand.pdb> <receptor.pdb>
    """
    import time
    import argparse

    # Start time
    start_time = time.time()

    # Overrides method in HelpFormatter
    class CapitalisedHelpFormatter(argparse.HelpFormatter):
        def add_usage(self, usage, actions, groups, prefix=None):
            if prefix is None:
                prefix = "Usage: "
            return super(CapitalisedHelpFormatter, self).add_usage(
                usage, actions, groups, prefix
            )

    parser = argparse.ArgumentParser(
        prog="lig2grid",
        description="Inserts a target ligand to a 3D grid created based on the \
            receptor, a padding and a grid spacing (step) and saves grid to a \
            PDB-formatted file",
        formatter_class=CapitalisedHelpFormatter,
        add_help=True,
    )

    # Change parser titles
    parser._positionals.title = "Positional arguments"
    parser._optionals.title = "Optional arguments"

    # Positional arguments
    parser.add_argument(
        "ligand",
        metavar="<ligand.pdb>",
        type=os.path.abspath,
        help="Path to a target ligand file.",
    )
    parser.add_argument(
        "receptor",
        metavar="<receptor.pdb>",
        type=os.path.abspath,
        help="Path to a target receptor file.",
    )

    # Optional arguments
    parser.add_argument(
        "-v",
        "--verbose",
        help="Print extra information to standard output.",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "--version",
        action="version",
        version="lig2grid v0.1.1",
        help="Show lig2grid version number and exit.",
    )
    parser.add_argument(
        "-p",
        "--padding",
        metavar="<float>",
        default=4.0,
        type=float,
        help="A length (\u212B) to be added in each direction \
            of the 3D grid. (default: %(default).1lf)",
    )
    parser.add_argument(
        "-s",
        "--step",
        metavar="<float>",
        default=0.6,
        type=float,
        help="Grid spacing. (default: %(default).1lf)",
    )
    parser.add_argument(
        "--ignore_h",
        action="store_false",
        default=True,
        help="Whether to ignore hydrogen atoms. (default: %(default)s)",
    )
    parser.add_argument(
        "-o",
        "--output",
        metavar="<str>",
        type=os.path.abspath,
        default=os.path.abspath("./output.pdb"),
        help="Output PDB-formatted file. (default: %(default)s)",
    )
    parser.add_argument(
        "--nthreads",
        metavar="<int>",
        type=int,
        default=os.cpu_count() - 1,
        help="Number of threads to apply in parallel routines\
            (default: %(default)s)",
    )

    # Parse command-line arguments
    args = parser.parse_args()

    # Run lig2grid
    lig2grid(
        args.ligand,
        args.receptor,
        args.padding,
        args.step,
        args.output,
        None,
        None,
        args.ignore_h,
        args.nthreads,
    )

    # Elapsed time
    elapsed_time = time.time() - start_time
    print(f"[ \033[1mElapsed time:\033[0m {elapsed_time:.4f} ]")

    return None


def cli_r2g():
    """
    rec2grid Command Line Interface (CLI)

    Parameters
    ----------
        None

    Returns
    -------
        None

    Example
    -------
    Usage: rec2grid [-h] [-v] [--version] [-p <float>] [-s <float>] \
        [--ignore_h] [-o <str>] [--nthreads <int>] <receptor.pdb>
    """
    import time
    import argparse

    # Start time
    start_time = time.time()

    # Overrides method in HelpFormatter
    class CapitalisedHelpFormatter(argparse.HelpFormatter):
        def add_usage(self, usage, actions, groups, prefix=None):
            if prefix is None:
                prefix = "Usage: "
            return super(CapitalisedHelpFormatter, self).add_usage(
                usage, actions, groups, prefix
            )

    parser = argparse.ArgumentParser(
        prog="lig2grid",
        description="Inserts a target receptor to a 3D grid created based on the \
            receptor, a padding and a grid spacing (step) and saves grid to a \
            PDB-formatted file",
        formatter_class=CapitalisedHelpFormatter,
        add_help=True,
    )

    # Change parser titles
    parser._positionals.title = "Positional arguments"
    parser._optionals.title = "Optional arguments"

    # Positional arguments
    parser.add_argument(
        "receptor",
        metavar="<receptor.pdb>",
        type=os.path.abspath,
        help="Path to a target receptor file.",
    )

    # Optional arguments
    parser.add_argument(
        "-v",
        "--verbose",
        help="Print extra information to standard output.",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "--version",
        action="version",
        version="lig2grid v0.1.1",
        help="Show lig2grid version number and exit.",
    )
    parser.add_argument(
        "-p",
        "--padding",
        metavar="<float>",
        default=4.0,
        type=float,
        help="A length (\u212B) to be added in each direction \
            of the 3D grid. (default: %(default).1lf)",
    )
    parser.add_argument(
        "-s",
        "--step",
        metavar="<float>",
        default=0.6,
        type=float,
        help="Grid spacing. (default: %(default).1lf)",
    )
    parser.add_argument(
        "--ignore_h",
        action="store_false",
        default=True,
        help="Whether to ignore hydrogen atoms. (default: %(default)s)",
    )
    parser.add_argument(
        "-o",
        "--output",
        metavar="<str>",
        type=os.path.abspath,
        default=os.path.abspath("./output.pdb"),
        help="Output PDB-formatted file. (default: %(default)s)",
    )
    parser.add_argument(
        "--nthreads",
        metavar="<int>",
        type=int,
        default=os.cpu_count() - 1,
        help="Number of threads to apply in parallel routines\
            (default: %(default)s)",
    )

    # Parse command-line arguments
    args = parser.parse_args()

    # Run lig2grid
    rec2grid(
        args.receptor,
        args.padding,
        args.step,
        args.output,
        None,
        None,
        args.ignore_h,
        args.nthreads,
    )

    # Elapsed time
    elapsed_time = time.time() - start_time
    print(f"[ \033[1mElapsed time:\033[0m {elapsed_time:.4f} ]")

    return None

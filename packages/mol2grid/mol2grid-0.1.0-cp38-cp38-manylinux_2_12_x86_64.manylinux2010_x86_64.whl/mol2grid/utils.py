import os
import numpy
import logging
from typing import Tuple, Union, Callable, Dict, List

# TODO:
# - Fix docstring
# - Create unittest

__all__ = ["read_vdw", "read_catalog", "read_mol", "define_grid"]

here = os.path.abspath(os.path.dirname(__file__))
vdw_cfg = os.path.join(here, "data/vdw.dat")
catalog_cfg = os.path.join(here, "data/catalog.dat")


def read_catalog(fn: str = catalog_cfg) -> Dict[str, int]:
    """[summary]

    Parameters
    ----------
    fn : str, optional
        [description], by default catalog_cfg

    Returns
    -------
    Dict[str, int]
        [description]
    """
    catalog = {}

    # Read catalog file
    with open(fn, "r") as f:
        # Read line by line
        for line in f.read().strip().strip(" ").strip("\t").splitlines():
            # Ignore commented lines
            if not line.startswith("#"):
                try:
                    atom, code = line.split("\t")
                except ValueError:
                    if len(line.split("\t")) != 2:
                        raise ValueError(
                            "A line in `catalog` has incorrect format. The values must be tab-separated."
                        )
                try:
                    catalog[atom] = int(code)
                except ValueError:
                    raise ValueError(
                        "A line in `catalog` has an incorrect integer number for an atom."
                    )
        # Include a code for missing values
        catalog["UNK"] = max(catalog.values()) + 1

    return catalog


def read_vdw(fn: str = vdw_cfg) -> Dict[str, Dict[str, Dict[str, float]]]:
    """Reads van der Waals radii from .dat file

    Parameters
    ----------
        fn (str): a path to a van der Waals radii file

    Returns
    -------
        vdw (dict): a dictionary containing radii values (vdw[resname][atom])

    Note
    ----
        The van der Waals radii file defines the radius values for each atom
        by residue and when not defined, it uses a generic value based on the
        atom type (check van der Waals File Template). The package contains a
        built-in van der Waals radii file: `vdw.dat`.

    See Also
    --------
        The van der Waals file template is the following:
        >RES
        C       1.66
        CA      2.00
        N       1.97
        O       1.69
        H       0.91
    """
    vdw = {}
    with open(fn, "r") as f:
        # Read line with data only (ignore empty lines)
        lines = [
            line.replace(" ", "")
            for line in f.read().splitlines()
            if line.replace("\t\t", "")
        ]
        for line in lines:
            if not line.startswith("#"):
                if line.startswith(">"):
                    res = line.replace(">", "").replace("\t\t", "").replace(" ", "")
                    vdw[res] = {}
                else:
                    try:
                        atom, radius = line.split("\t\t")
                    except ValueError:
                        if len(line.split("\t\t")) != 2:
                            raise ValueError(
                                "A line in `vdw` has incorrect format. The values must be double tab-separated."
                            )
                    try:
                        vdw[res][atom] = float(radius)
                    except ValueError:
                        raise ValueError(
                            "A line in `vdw` has an incorrect radius type for an atom."
                        )
    return vdw


def _process_pdb_line(
    line: str, vdw: Dict[str, Dict[str, Dict[str, float]]], catalog: Dict[str, int]
) -> List[float]:
    """
    Extracts ATOM and HETATM information of PDB line

    Parameters
    ----------
        line (str): line of PDB file
        vdw (dict): Dictionary with radii values (vdw[resname][atom])

    Returns
    -------
        coords (list): a list with xyz coordinates and radius
    """
    # Get PDB information
    atom = line[12:16].strip()
    resname = line[17:20].strip()
    x = float(line[30:38])
    y = float(line[38:46])
    z = float(line[46:54])
    atom_symbol = line[76:78].strip().upper()

    # Get atom radius from vdw
    if resname in vdw.keys() and atom in vdw[resname].keys():
        radius = vdw[resname][atom]
    else:
        radius = vdw["GEN"][atom_symbol]
        logging.info(
            f"Warning: Atom {atom} of residue {resname} \
            not found in dictionary"
        )
        logging.info(
            f"Warning: Using generic atom {atom_symbol} \
            radius: {radius} \u00c5"
        )

    # Get atom code
    if atom_symbol in catalog.keys():
        code = catalog[atom_symbol]
    else:
        code = catalog["UNK"]

    # Prepare output
    xyzrc = [x, y, z, radius, code]

    return xyzrc


# TODO: ignore H flag?


def read_mol(
    fn: str,
    vdw: Union[Dict[str, Dict[str, Dict[str, float]]], Callable] = read_vdw(),
    catalog: Union[Dict[str, int], Callable] = read_catalog(),
) -> Tuple[numpy.ndarray, numpy.ndarray]:
    """Reads PDB file into Numpy arrays

    Parameters
    ----------
        fn (str): a path to PDB file
        vdw (dict): a dictionary with radii values (vdw[resname][atom])

    Returns
    -------
        atominfo (numpy.ndarray): a numpy array with atomic information
        (residue number, chain, residue name, atom name)
        xyzrc (numpy.ndarray): a numpy array with xyz atomic coordinates
        and radii values (x, y, z, radius)

    Note
    ----
        The vdW radii file defines the radius values for each atom by
        residue and when not defined, it uses a generic value based on
        the atom type.
    """
    xyzrc = []
    with open(fn, "r") as f:
        for line in f.readlines():
            if line[:4] == "ATOM" or line[:6] == "HETATM":
                xyzrc.append(_process_pdb_line(line, vdw, catalog))
    return numpy.asarray(xyzrc)


def _get_vertices(
    xyzrc: Union[numpy.ndarray, List],
    padding: Union[float, int],
    step: Union[float, int] = 0.6,
) -> numpy.ndarray:
    """Gets 3D grid vertices from a list of atom coordinates, considering
    a padding and a step (grid spacing)

    Parameters
    ----------
    xyzrc : Union[numpy.ndarray, List]
        A numpy array with xyz atomic coordinates
    padding : Union[float, int]
        A length to be added in each direction
    step : Union[float, int], optional
        Grid spacing, by default 0.6

    Returns
    -------
    numpy.ndarray
        A numpy array with xyz vertices coordinates
        (origin, X-axis, Y-axis, Z-axis)

    Raises
    ------
    TypeError
        `xyzrc` must be a list or a numpy.ndarray
    TypeError
        `padding` must be a non-negative real number
    TypeError
        `step` must be a non-negative real number
    ValueError
        `xyzrc` has incorrect shape. It must be (, 5)
    """
    if type(xyzrc) not in [numpy.ndarray, list]:
        raise TypeError("`xyzrc` must be a list or a numpy.ndarray.")
    if type(padding) not in [int, float]:
        raise TypeError("`padding` must be a non-negative real number.")
    if type(step) not in [int, float]:
        raise TypeError("`step` must be a non-negative real number.")
    if len(numpy.asarray(xyzrc).shape) != 2:
        raise ValueError("`xyzrc` has incorrect shape. It must be (n, 5)")
    elif numpy.asarray(xyzrc).shape[1] != 5:
        raise ValueError("`xyzrc` has incorrect shape. It must be (n, 5).")

    # Convert xyzrc type
    if type(xyzrc) == list:
        xyzrc = numpy.asarray(xyzrc)

    # Prepare vertices
    P1 = numpy.min(xyzrc[:, 0:3], axis=0) - padding - step
    xmax, ymax, zmax = numpy.max(xyzrc[:, 0:3], axis=0) + padding + step
    P2 = numpy.array([xmax, P1[1], P1[2]])
    P3 = numpy.array([P1[0], ymax, P1[2]])
    P4 = numpy.array([P1[0], P1[1], zmax])

    # Pack vertices
    vertices = numpy.array([P1, P2, P3, P4])

    return vertices


def _get_sincos(vertices: Union[numpy.ndarray, List]) -> numpy.ndarray:
    """Gets sine and cossine of the grid rotation angles from a list of vertices
    coordinates

    Parameters
    ----------
    vertices : Union[numpy.ndarray, List]
        A list of xyz vertices coordinates (origin, X-axis, Y-axis, Z-axis)

    Returns
    -------
    numpy.ndarray
        A numpy.ndarray with sine and cossine of the grid rotation
        angles (sina, cosa, sinb, cosb)

    Raises
    ------
    TypeError
        `vertices` must be a list or a numpy.ndarray
    ValueError
        `vertices` has incorrect shape
    """
    if type(vertices) not in [numpy.ndarray, list]:
        raise TypeError("`vertices` must be a list or a numpy.ndarray.")
    if numpy.asarray(vertices).shape != (4, 3):
        raise ValueError("`vertices` has incorrect shape.")

    # Convert type
    if type(vertices) == list:
        vertices = numpy.asarray(vertices)

    # Unpack vertices
    P1, P2, P3, P4 = vertices

    # Calculate distance between points
    norm1 = numpy.linalg.norm(P2 - P1)
    norm2 = numpy.linalg.norm(P3 - P1)
    norm3 = numpy.linalg.norm(P4 - P1)

    # Calculate sin and cos of angles a and b
    sincos = numpy.array(
        [
            (P4[1] - P1[1]) / norm3,  # sin a
            (P3[1] - P1[1]) / norm2,  # cos a
            (P2[2] - P1[2]) / norm1,  # sin b
            (P2[0] - P1[0]) / norm1,  # cos b
        ]
    )

    return sincos


def _get_dimensions(
    vertices: Union[numpy.ndarray, List], step: float = 0.6
) -> Tuple[int, int, int]:
    """Gets dimensions of 3D grid from vertices

    Parameters
    ----------
    vertices : Union[numpy.ndarray, List]
        A numpy array with xyz vertices coordinates (origin, X-axis, Y-axis, Z-axis)
    step : float, optional
        Grid spacing (A), by default 0.6

    Returns
    -------
    Tuple[int, int, int]
        Grid units in x-, y- and z-axis

    Raises
    ------
    TypeError
        `vertices` must be a list or a numpy.ndarray
    ValueError
        `vertices` has incorrect shape
    TypeError
        `step` must be a non-negative real number
    """
    if type(vertices) not in [numpy.ndarray, list]:
        raise TypeError("`vertices` must be a list or a numpy.ndarray.")
    if numpy.asarray(vertices).shape != (4, 3):
        raise ValueError("`vertices` has incorrect shape.")
    if type(step) not in [float, int] and step > 0.0:
        raise TypeError("`step` must be a non-negative real number.")

    # Convert type
    if type(vertices) == list:
        vertices = numpy.asarray(vertices)

    # Unpack vertices
    P1, P2, P3, P4 = vertices

    # Calculate distance between points
    norm1 = numpy.linalg.norm(P2 - P1)
    norm2 = numpy.linalg.norm(P3 - P1)
    norm3 = numpy.linalg.norm(P4 - P1)

    # Calculate grid dimensions
    nx = int(norm1 / step) + 1 if norm1 % step != 0 else int(norm1 / step)
    ny = int(norm2 / step) + 1 if norm1 % step != 0 else int(norm1 / step)
    nz = int(norm3 / step) + 1 if norm1 % step != 0 else int(norm1 / step)

    return nx, ny, nz


def define_grid(
    xyzrc: numpy.ndarray, padding: float, step: float = 0.6
) -> Tuple[numpy.ndarray, numpy.ndarray, int, int, int]:
    """[summary]

    Parameters
    ----------
    xyzrc : numpy.ndarray
        [description]
    padding : float
        [description]
    step : float, optional
        [description], by default 0.6

    Returns
    -------
    Tuple[numpy.ndarray, numpy.ndarray, int, int, int]
        [description]

    Raises
    ------
    TypeError
        [description]
    ValueError
        [description]
    TypeError
        [description]
    TypeError
        [description]
    """
    if type(xyzrc) not in [numpy.ndarray, list]:
        raise TypeError("`xyzrc` must be a list or a numpy.ndarray.")
    if len(numpy.asarray(xyzrc).shape) != 2:
        raise ValueError("`xyzrc` has incorrect shape. It must be (n, 5)")
    elif numpy.asarray(xyzrc).shape[1] != 5:
        raise ValueError("`xyzrc` has incorrect shape. It must be (n, 5).")
    if type(padding) not in [float, int]:
        raise TypeError("`padding` must be a non-negative real number.")
    if type(step) not in [float, int] and step > 0.0:
        raise TypeError("`step` must be a non-negative real number.")

    # Convert type
    if type(xyzrc) == list:
        xyzrc = numpy.asarray(xyzrc)

    # Define vertices
    vertices = _get_vertices(xyzrc, padding, step)

    # Unpack origin from vertices
    origin, _, _, _ = vertices

    # Define sine and cossine
    sincos = _get_sincos(vertices)

    # Define grid dimensions
    nx, ny, nz = _get_dimensions(vertices, step)

    return origin, sincos, nx, ny, nz

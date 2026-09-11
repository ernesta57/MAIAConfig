import os
from k4FWCore.parseArgs import parser
from Common.argutils import add_argument_once

def get_digi_args():
    # Shared with reco_args; added once so the two can be combined in one job.
    add_argument_once(
        parser,
        "--DD4hepXMLFile",
        help="Compact detector description file",
        type=str,
        default=os.environ.get("k4geo_DIR", "")+"/MuColl/MAIA/compact/MAIA_v0/MAIA_v0.xml",
    )

    parser.add_argument(
        "--OverlayFullPathToMuPlus",
        help="Path to files for muplus BIB overlay",
        type=str,
        default="/path/to/muplus/",
    )

    parser.add_argument(
        "--OverlayFullPathToMuMinus",
        help="Path to files for muminus BIB overlay",
        type=str,
        default="/path/to/muminus/",
    )

    parser.add_argument(
        "--OverlayFullNumberBackground",
        help="Number of background files used for BIB overlay",
        type=int,
        default=1666, #Magic number for EU24 BIB
    )

    parser.add_argument(
        "--OverlayIPBackgroundFileNames",
        help="Path(s) to file(s) used for incoherent pairs overlay",
        type=str,
        nargs="+",
        default=["/path/to/pairs.edm4hep.root"],
    )

    parser.add_argument(
        "--doOverlayFull",
        help="Do BIB overlay",
        action="store_true",
        default=False,
    )

    parser.add_argument(
        "--doOverlayIP",
        help="Do incoherent pairs overlay",
        action="store_true",
        default=False,
    )

    parser.add_argument(
        "--doFilterDL",
        help="Do double-layer filtering",
        action="store_true",
        default=False,
    )

    # Shared with reco_args (the merger reads the coned hits when enabled).
    add_argument_once(
        parser,
        "--doTrackerConing",
        help="Filter tracker hits into cones around the signal MC particles (BIB cleaning)",
        action="store_true",
        default=False,
    )

    parser.add_argument(
        "--RandSeed",
        help="Random seed for digitization",
        type=int,
        default=42,
    )

    parser.add_argument(
        "--doRealisticDigi",
        help="Toggle realistic digitization",
        action="store_true",
        default=False,
    )    

    parser.add_argument(
        "--doTimeWindowFilter",
        help="Apply TrackerHitTimeWindowFilter to the realistic digitization output",
        action="store_true",
        default=False,
    )

    parser.add_argument(
        "--do3DDigi",
        help="Use Realistic3DDigitiser instead of MuonCVXDDigitiser for the subdetectors listed in --Detectors3D. --doRealisticDigi must be set",
        action="store_true",
        default=False,
    )

    parser.add_argument(
        "--Detectors3D",
        help="Which subdetector regions use the Realistic3DDigitiser when --do3DDigi is set",
        type=str,
        nargs="+",
        default=["VXDBarrel"],
        choices=["VXDBarrel", "VXDEndcap"],
    )

    the_args = parser.parse_known_args()[0]

    if the_args.do3DDigi and not the_args.doRealisticDigi:
        parser.error("--do3DDigi requires --doRealisticDigi to also be set")

    return the_args
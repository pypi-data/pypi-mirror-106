Command Line Interface
======================

For common calibration procedures, lhcb_ftcalib can be called via the command line via the 
executable `ftcalib`.
::
    ftcalib --help

    usage: ftcalib [-h] [-t TAGGERS [TAGGERS ...]] [-SS SSTAGGERS [SSTAGGERS ...]]
                   [-OS OSTAGGERS [OSTAGGERS ...]] [-id ID_BRANCH]
                   [-mode {Bu,Bd,Bs}] [-tau TAU] [-tauerr TAUERR]
                   [-timeunit {ns,ps,fs}] [-weights WEIGHTS] -op
                   {calibrate,combine,apply} [{calibrate,combine,apply} ...]
                   [-write WRITE] [-selection SELECTION] [-input_cal INPUT_CAL]
                   [-plot STORE_TRUE] [-fun FUN FUN]
                   [-link {mistag,logit,rlogit,probit,rprobit,cauchit,rcauchit}]
                   [-i]
                   rootfile

    LHCb Flavour Tagging calibration software

    positional arguments:
      rootfile              ROOT file and tree to read tagging data from.
                            (example: "file.root:DecayTree")

    optional arguments:
      -h, --help            show this help message and exit
      -t TAGGERS [TAGGERS ...]
                            Enumeration of taggers to find in file. This argument
                            will try to match partial names, e.g.
                            "MuonLatest"->"B_OSMuonLatest_TAGDEC/ETA"
      -SS SSTAGGERS [SSTAGGERS ...]
                            Enumeration of same side taggers to find in file. This
                            argument will try to match partial names, e.g.
                            "MuonLatest"->"B_OSMuonLatest_TAGDEC/ETA"
      -OS OSTAGGERS [OSTAGGERS ...]
                            Enumeration of opposite side taggers to find in file.
                            This argument will try to match partial names, e.g.
                            "MuonLatest"->"B_OSMuonLatest_TAGDEC/ETA"
      -id ID_BRANCH         Name of the B meson id branch
      -mode {Bu,Bd,Bs}      Calibration mode
      -tau TAU              Name of the decay time branch
      -tauerr TAUERR        Name of the decay time uncertainty branch
      -timeunit {ns,ps,fs}  Decay time unit
      -weights WEIGHTS      Name of the per-event weight branch
      -op {calibrate,combine,apply} [{calibrate,combine,apply} ...]
                            What to do with the loaded taggers
      -write WRITE          Name of a root file where to store calibrated branches
      -selection SELECTION  Selection expression (example: 'eventNumber%2==0')
      -input_cal INPUT_CAL  JSON file of the input calibrations
      -plot STORE_TRUE      If set, plots calibration curves
      -fun FUN FUN          CalibrationFunction followed by degree (default:
                            ['POLY', 1])
      -link {mistag,logit,rlogit,probit,rprobit,cauchit,rcauchit}
                            Link function (default: mistag)
      -i                    Interactive mode, will ask for confirmation

Calibrating a set of taggers
.......................................
To calibrate the vertex charge tagger "OSVtxCh_TAGDEC/ETA" and the OS Charm tagger "OSCharm_TAGDEC/ETA"
we list the two taggers as tagger name hints via `-t`, specify an id Branch and we choose B+ as the calibration
mode. Then we specify what operations should be performed via the option `-op`. In this case we just 
want to "calibrate" the taggers. Lastly, we specify an output file pattern for the calibrations and calibrated mistag branches via `-write`.
::
    ftcalib file.root:DecayTree -t Vtx Charm -id B_ID -mode Bu -op calibrate -write vtxAndCharm

Calibrating and combining taggers
.................................
::
    ftcalib file.root:DecayTree -OS Vtx Charm -SS SSPion SSProton -id B_ID -mode Bu -op calibrate combine calibrate -write calib_result

Calibrating taggers in a file and applying the calibrations
...........................................................
Applying calibration is done in a separate step. First, we determine calibrations on a control channel and then we use the 
calibration file as the input calibration for some target data.
::
    ftcalib file.root:DecayTree -OS Vtx Charm -SS SSPion SSProton -id B_ID -mode Bu -op calibrate combine calibrate -write calib_result
    ftcalib targetdata.root:DecayTree -OS Vtx Charm -SS SSPion SSProton -op apply combine -write applied_calibration -input_cal calib_result.json

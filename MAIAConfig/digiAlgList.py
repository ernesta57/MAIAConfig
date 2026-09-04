from GaudiKernel.Constants import INFO, WARNING

def makeDigiAlgList(the_args):
    '''-------------------------------------------------------------'''
    '''    Add the Digitization Algorithms to the Algorithm List    '''
    '''-------------------------------------------------------------'''
    algList = []
    # Event Counter
    from Common.event_counter import event_counter_cfg
    algList.append(event_counter_cfg())

    # BIB Overlay
    if the_args.doOverlayFull:
        from Overlay.overlay_BIB import overlay_full_cfg
        algList.append(overlay_full_cfg(the_args))

    # Incoherent Pair (IP) Overlay (chained after BIB if both are enabled)
    if the_args.doOverlayIP:
        from Overlay.overlay_IP import overlay_ip_cfg
        algList.append(overlay_ip_cfg(the_args))

    # Tracker Digitization
    if (the_args.doRealisticDigi):
        from TrackerDigi.tracking_vertex import new_VXDBarrel_Realistic, new_VXDEndcap_Realistic
        from TrackerDigi.tracking_inner import new_ITBarrel_Realistic, new_ITEndcap_Realistic
        from TrackerDigi.tracking_outer import new_OTBarrel_Realistic, new_OTEndcap_Realistic
        algList.append(new_VXDBarrel_Realistic(the_args))
        algList.append(new_VXDEndcap_Realistic(the_args))
        algList.append(new_ITBarrel_Realistic(the_args))
        algList.append(new_ITEndcap_Realistic(the_args))
        algList.append(new_OTBarrel_Realistic(the_args))
        algList.append(new_OTEndcap_Realistic(the_args))
    else:
        from TrackerDigi.tracking_vertex import new_VXDBarrel, new_VXDEndcap
        from TrackerDigi.tracking_inner import new_ITBarrel, new_ITEndcap
        from TrackerDigi.tracking_outer import new_OTBarrel, new_OTEndcap
        algList.append(new_VXDBarrel(the_args))
        algList.append(new_VXDEndcap(the_args))
        algList.append(new_ITBarrel(the_args))
        algList.append(new_ITEndcap(the_args))
        algList.append(new_OTBarrel(the_args))
        algList.append(new_OTEndcap(the_args))

    # Tracker Hit Coning (BIB cleaning). When enabled the merger downstream reads
    # the "...Coned" collections produced here (see Tracking/mergers.py).
    if the_args.doTrackerConing:
        from TrackerDigi.coning import tracker_coner_cfgs
        algList += tracker_coner_cfgs(the_args)

    # EM, Hadronic Calorimeter Digitization
    from CaloDigi.calorimetry_EM import ECalBarrelDigi_cfg, ECalBarrelReco_cfg
    from CaloDigi.calorimetry_EM import ECalEndcapDigi_cfg, ECalEndcapReco_cfg
    algList.append(ECalBarrelDigi_cfg(the_args))
    algList.append(ECalBarrelReco_cfg())
    algList.append(ECalEndcapDigi_cfg(the_args))
    algList.append(ECalEndcapReco_cfg())
    from CaloDigi.calorimetry_HAD import HCalBarrelDigi_cfg, HCalBarrelReco_cfg
    from CaloDigi.calorimetry_HAD import HCalEndcapDigi_cfg, HCalEndcapReco_cfg
    algList.append(HCalBarrelDigi_cfg(the_args))
    algList.append(HCalBarrelReco_cfg())
    algList.append(HCalEndcapDigi_cfg(the_args))
    algList.append(HCalEndcapReco_cfg())

    # Calorimeter Hit Coning + BIB Selection. Always run, mirroring steer_reco.py:
    # each region is coned around the signal MC particles and then thresholded,
    # producing the "...Sel" collections that Pandora consumes.
    from CaloDigi.calo_coning import calo_coner_cfgs, calo_selector_cfgs
    algList += calo_coner_cfgs()
    algList += calo_selector_cfgs()

    # Muon Calorimeter Digitization
    from CaloDigi.calorimetry_MU import MuonBarrelDigi_cfg, MuonEndcapDigi_cfg
    algList.append(MuonBarrelDigi_cfg(the_args))
    algList.append(MuonEndcapDigi_cfg(the_args))

    # Vertex Filtering
    if the_args.doFilterDL:
        from Tracking.filterDL_vertex import filterDL_vertexBarrel_cfg, filterDL_vertexEndcap_cfg
        algList.append(filterDL_vertexBarrel_cfg())
        algList.append(filterDL_vertexEndcap_cfg())

    return algList
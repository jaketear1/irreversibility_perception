Data folder --
# EEG data information (eeg.npy)
- Dimensions: 45410 x 64 x 166 (trial x channel x time)
- Sampling frequency: 128Hz
- Epoch time-window: -500ms to 790ms 
- Epoch times can be retrieved via: np.linspace(-0.5, 0.790,166)
- EEG channels (64, in order of data): 
	‘Fp1', 'AF7', 'AF3', 'F1', 'F3', 'F5', 'F7', 'FT7', 'FC5', 'FC3',
	'FC1', 'C1', 'C3', 'C5', 'T7', 'TP7', 'CP5', 'CP3', 'CP1', 'P1',
	'P3', 'P5', 'P7', 'P9', 'PO7', 'PO3', 'O1', 'Iz', 'Oz', 'POz',
	'Pz', 'CPz', 'Fpz', 'Fp2', 'AF8', 'AF4', 'AFz', 'Fz', 'F2', 'F4',
	'F6', 'F8', 'FT8', 'FC6', 'FC4', 'FC2', 'FCz', 'Cz', 'C2', 'C4',
	'C6', 'T8', 'TP8', 'CP6', 'CP4', 'CP2', 'P2', 'P4', 'P6', 'P8',
	'P10', 'PO8', 'PO4', 'O2’


# Behavior data information (behavior.csv)
- Dimensions: 45410 x 14 (trial x trial variable)
- Note: behavioral data and EEG data are aligned in trial (e.g. 10th trial in behavioral data corresponds to 10th trial in neural data)
- The 14 trial variables are:
	1. Subject number
	2. Drug (ATX: atomoxetine, DNP: donepezil, PLC: placebo)
	3. Experimental session (drug sessions were counterbalanced)
	4. Block (each task was subdivided in two major blocks
	5. Miniblock (each block was subdivided in several miniblocks of 70 trials)
	6. Trial number (note there are gaps here > rejected epochs or omitted data because of eyeblinks/no behavioral response)
	7.  Cue (0=left | 1=right)
	8. Target stimulus location (0=left | 1=right)
	9. Cue validity (cue x location congruency, 0=invalid | 1=valid)
	10. Stimulus orientation (0=CCW | 1=CW)
	11. Response (0=left button/CCW | 1=right button/CW)
	12. Correctness (stimulus x response congruency,  0=incorrect | 1=correct
	13. RT (in ms)
	14. Total trial number, index of the 45410 trials. 
	15. Baseline pupil size (in pixels), time-window -500ms to 0ms pre-stimulus.

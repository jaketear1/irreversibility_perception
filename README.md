# irreversibility_perception

This repo comprises the code for my Master's thesis: "Irreversibility of EEG Data in Perceptual Decision Making", defended July 30th, 2024, supervised by Dr. Gustavo Deco.

It's not perfect, but when I began in January 2024 I didn't really know how to organize all this stuff.

Thesis attached. Please read thesis before the code.

## Navigating the folders
### data/
This folder contains the behavioral and EEG data from the visual discrimination task of [Beerendonk et al., (2024)]([url](https://www.pnas.org/doi/full/10.1073/pnas.2312898121)). As well as: FowRev_long_26to89_tau5.mat, FowRev_long_90to153_tau5.mat, FowRev_long_192to255_tau5.mat, and FowRev_long_256to319_tau5.mat, which are the irreversibility reference matrices of each task trial for the pre-cue, post-cue, pre-stimulus, and post-stimulus epochs respectively. It also contains the pre- and post-stimulus 1/f slopes for each trial (averaged across all electrodes), pre- and post-stimulus alpha power of each electrode for each trial, and pre- and post-stimulus sample entropy of each electrode for each trial.
(1/f slope = aperiodic exponent, see [Donoghue et al., (2020a)]([url](https://www.nature.com/articles/s41593-020-00744-x)))

### scripts/
1) binning_analysis.ipynb, used to replicate the pupil bin X perceptual sensitivity (d') graph in Beerendonk et al., 2024, as well as adapting the binning procedure for irreversibility, 1/f slope, alpha power, and other values to make comparisons. Contains exploratory analysis, scatterplots, statistical tests, and visualizations. 
2) running_irrev.ipynb, used to compute irreversibility, alpha power, 1/f slope, and sample entropy values, creating those corresponding files of the data/ folder.
3) simulations.ipynb, used to compare irreversibility values computed over simulated EEG data with varying oscillatory schemes, added noise, amplitude changes, as well as with phase lag vs. phase synchrony.

### results/
Contains the figures I used plus my thesis defense powerpoint. Will house SVG files for the figures of the paper we are preparing.

### src/
This is a placeholder, but shows I now recognize the value of separating functions from notebooks.

### tests/
Mostly bad code used to test things like source localization with MNE, Lempel Ziv complexity, and performing PCA on EEG data. The only relevant file to the thesis is first_trial_sanity.ipynb, which investigates the EEG data of trials with outlier irreversibility or alpha power values.


## Acknowledgements
I dedicate this work to my late Papa, who supported my education in every possible way. And to my parents. I thank Elvira del Agua for her time and attention spent wrestling with code and concepts. And Gustavo Deco for allowing me to explore his groundbreaking thoughts and theories, for his guidance, and for bringing together such brilliant minds in the group. I thank Luca Bonatti for coordinating the Master's program with rigor, compassion, and humor. And to my cohort for making Barcelona so enjoyable. I thank ChatGPT, of which my use resembled a form of prayer. And finally, to the dreamers of the golden neuroscience dream, those who believe that brain data is a secret journal written in a language we are yet to fully understand.


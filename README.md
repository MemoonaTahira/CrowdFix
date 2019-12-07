CrowdFix
=========

Detail of the dataset and its analysis can be found in our arXiv preprint [here](https://arxiv.org/abs/1910.02618v2).

## Brief introduction
CrowdFix includes **434 videos** with diverse crowd scenes, containing a total of **37,493 frames** and **1,249 seconds**. The diverse content refers to different crowd activities under three distinct categories - Sparse, Dense Free Flowing and Dense Congested. All videos are at 720p resolution and 30 Hz frame rate. For monitoring the eye movements, an EyeTribe eye tracker  was used in our experiment. **26 participants** (10 males and 16 females), aging from 17 to 40, participated in the eye-tracking experiment. All participants were non-experts for the eye-tracking experiment, with normal/corrected-to-normal vision. During the experiment, the distance between subjects and the monitor was fixed at 60 cm. Before viewing videos, each subject was required to perform a 9-point calibration for the eye tracker. After the calibration, the subjects were asked to free-view videos displayed in an MTV style. Finally,  fixations of all 32 subjects on 538 videos were collected for our eye-tracking database.

Some stills from the dataset videos are shown in [**examples**](/figs/ ). A sample of resultant heatmaps of eye fixations over a few videos are shown in in [**sample.avi**](sample.avi).

## How to use 
The dataset can be downloaded from the following [link](https://drive.google.com/drive/folders/1_7wKveiebIe16opBnIOMrRJzxASo9o4L?usp=sharing).

<pre> CrowdFix
  ┬ videos: 434 clips annotated with their category, 5GB 
  ├ frames.py: Run frame.py without modifying folder hierarchy to generate the frames with the same name sequence as the corresponding ground truth binary fixation and saliency maps.
  ├ Binary Fixation Maps
  └ Saliency Maps
</pre> 

              
**'CategoryInfo.xlsx'** lists the information of crowd categories against each video. It includes the following information:
* 'column 1' : Video Number as given in the uploaded video folder.
* 'column 2' : Crowd Category Type (SP for Sparse, DF for Dense Free-Flowing and DC for Dense Congested)



## Citation
You are welcome to freely use this database, and please cite with the following Bibtex code:

```
@ARTICLE{8918032,
author={M. {Tahira} and S. {Mehboob} and A. U. {Rahman} and O. {Arif}},
journal={IEEE Access},
title={CrowdFix: An Eyetracking Dataset of Real Life Crowd Videos},
year={2019},
volume={},
number={},
pages={1-1},
keywords={Videos;Visualization;Computational modeling;Gaze tracking;Predictive models;Meters;Licenses;Attention;Crowd Analysis;Crowd Videos;Eye movement;Eye tracking;Fixations;Region of Interest;Saliency},
doi={10.1109/ACCESS.2019.2956840},
ISSN={2169-3536},
month={},}
```

Feel free to contact mtahira.mscs17seecs@seecs.edu.pk / smehboob.mscs17seecs@seecs.edu.pk in case of any queries.





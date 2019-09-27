CrowdFix
=========
A new eye-tracking dataset called CrowdFix for crowd video saliency database from Memoona Tahira and Sobas Mehboob (National University of Sciences and Technology)


## Brief introduction
CrowdFix includes **434 videos** with diverse crowd scenes, containing a total of **37,493 frames** and **1,249 seconds**. The diverse content refers to different crowd activities under three distinct categories - Sparse, Dense Free Flowing and Dense Congested. All videos are at 720p resolution and 30 Hz frame rate. Then, for monitoring the eye movements, a EyeTribe eye tracker  was used in our experiment. Moreover, **26 participants** (10 males and 16 females), aging from 17 to 40, participated in the eye-tracking experiment. All participants were non-experts for the eye-tracking experiment, with normal/corrected-to-normal vision. During the experiment, the distance between subjects and the monitor was fixed at 60 cm. Before viewing videos, each subject was required to perform a 9-point calibration for the eye tracker. Afterwards, the subjects were asked to free-view videos displayed in an MTV style. Finally,  fixations of all 32 subjects on 538 videos were collected for our eye-tracking database.

Some examples of CrowdFix saliency heatmaps are shown below in ![**examples**](/figs/ ) and in ![**sample.mp4**](sample.mp4).

## How to use 
The dataset can be downloaded at [Dropbox](https://www.dropbox.com/s/pc8symd9i3cky1q/LEDOV.zip?dl=0) and [Google Drive](http://pan.baidu.com/s/1pLmfjCZ). The link contains the following folders and files:

<pre> CrowdFix
  ┬ videos: 434 clips annotated with their category, 5GB 
  ├ frames.py: Run frame.py without modifying folder hierarchy to generate the frames with the same name sequence as the corresponding ground truth binary fixation and saliency maps.
  ├ Binary Fixation Maps
  └ Saliency Maps
</pre> 

              
**'CategoryInfo.xlsx'** lists the information of crowd categories against each video. It includes the following information:
* 'column 1' *: Video Number as given in the uploaded video folder.
* 'column 2' *: Crowd Category Type (SP for Sparse, DF for Dense-Free Flowing and DC for Dense Congested)



## Citation
You are welcome to freely use this database, and please cite with the following Bibtex code:

```
@InProceedings{Jiang_2018_ECCV,
author = {Jiang, Lai and Xu, Mai and Liu, Tie and Qiao, Minglang and Wang, Zulin},
title = {DeepVS: A Deep Learning Based Video Saliency Prediction Approach},
booktitle = {The European Conference on Computer Vision (ECCV)},
month = {September},
year = {2018}
} 
```

## Contact
Should you have any queries, please contact mtahira.mscs17seecs@seecs.edu.pk / smehboob.mscs17seecs@seecs.edu.pk

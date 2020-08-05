## Tools for Evaluating SLAM Systems

### distance.py

This file is used to calculate the movement distance of the sensor.

```
python2 distance.py file_name
```

*The format of your text file should be " time_stamp tx ty tz ....."*

<img src="images/distance.png" alt="distance" style="zoom:50%;" />

### ate_trajectory.py

this file is used to calculate the ATE and trajectory for two input files, which is based on associate.py. 

<img src="images/ate_trajectory.png" alt="ate_trajectory" style="zoom: 50%;" />

```
python2 ate_trajectory.py gt.txt file1.txt file2.txt --verbose --plot trajectory.png
```



 




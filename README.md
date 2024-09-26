Distributed Acoustic Sensing (DAS) Data Analysis and Anomaly Detection
Introduction
This project focuses on the analysis of Distributed Acoustic Sensing (DAS) data, specifically targeting signal analysis, line detection, and anomaly detection. The analysis leverages several Python libraries, including Pandas, OpenCV, Scikit-learn, and Seaborn, to extract insights from the DAS data.

What is Distributed Acoustic Sensing (DAS)?
Distributed Acoustic Sensing (DAS) is an innovative technology that utilizes optical fiber cables to detect acoustic signals along the length of a pipeline. The fiber optic cable encircles the pipeline, providing continuous monitoring of fluid flow and various conditions within the pipeline.


Figure: Diagram illustrating the placement of optical fiber around a pipeline.

Dataset Overview and Initial Analysis
The DAS dataset is structured with rows representing depths and columns corresponding to time intervals in minutes. To gain an understanding of the dataset's characteristics, an initial statistical summary and visualizations were performed.

Overview of the Dataset

data.describe()
The output of the above code provides a statistical overview of the dataset.

Heatmap Visualization
To visualize the variation in signal strength over time and depth, a spatiotemporal heatmap was created.


Figure: Spatiotemporal heatmap illustrating changes in signal strength across depth and time.

Code for Heatmap

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
sns.heatmap(data, cmap='viridis')
plt.title('Spatiotemporal Heatmap of DAS Data')
plt.xlabel('Time (minutes)')
plt.ylabel('Depth (m)')
plt.show()
Signal Change at Selected Depths
Signal variation over time at specific depths (100m, 500m, and 1000m) was analyzed to observe potential patterns.

Line Plot of Signal Variation

Figure: Line plot showing signal variation over time at selected depths.

Code for Plotting

import matplotlib.pyplot as plt

selected_depths = [100, 500, 1000]
for depth in selected_depths:
    plt.plot(data.iloc[depth], label=f'Depth {depth}m')

plt.title('Signal Variation at Selected Depths')
plt.xlabel('Time (minutes)')
plt.ylabel('Signal Strength')
plt.legend()
plt.show()
Edge Detection
Using the Canny edge detection method, significant edges in the signal were highlighted, enhancing our ability to detect transitions in the data.

Canny Edge Detection Result

Figure: Result of Canny edge detection illustrating detected edges in the signal.

Code for Edge Detection

import cv2
import numpy as np

edges = cv2.Canny(data.values.astype(np.uint8), threshold1=30, threshold2=100)
plt.imshow(edges, cmap='gray')
plt.title('Canny Edge Detection Result')
plt.axis('off')
plt.show()
Line Detection with DBSCAN
Following edge detection, the DBSCAN clustering algorithm was employed to identify lines within the data.

Scatter Plot of Detected Lines

Figure: Scatter plot showing detected lines using DBSCAN, color-coded by clusters.

Code for DBSCAN

from sklearn.cluster import DBSCAN

dbscan = DBSCAN(eps=0.5, min_samples=5)
clusters = dbscan.fit_predict(data)
plt.scatter(data.index, data.values, c=clusters, cmap='plasma')
plt.title('Line Detection using DBSCAN')
plt.xlabel('Time')
plt.ylabel('Signal Strength')
plt.show()
Anomaly Detection with Isolation Forest
The Isolation Forest algorithm was utilized to detect anomalies within the DAS data, setting a contamination rate of 1% to identify unusual signal behaviors.

Anomaly Detection Visualization

Figure: Visualization of detected anomalies in the DAS data.

Code for Anomaly Detection

from sklearn.ensemble import IsolationForest

clf = IsolationForest(contamination=0.01, random_state=42)
clf.fit(data)
anomalies_ml = clf.predict(data)
data['Anomaly'] = anomalies_ml
anomalies_detected = data[data['Anomaly'] == -1]
Results and Conclusion
The analyses conducted throughout this project have yielded significant insights:

Signal Analysis: Patterns in signal strength were identified across different depths.
Edge Detection: The identification of edges highlighted crucial transitions in the signal.
Anomaly Detection: Anomalies were successfully detected, pointing to unexpected behaviors at specific depths.
Conclusion
These analyses provide essential tools for monitoring pipeline conditions, enabling early detection of potential issues that could affect safety and operational efficiency.


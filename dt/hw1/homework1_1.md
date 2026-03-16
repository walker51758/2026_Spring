# 作业一

![image-20260312093347563](./../../../../Pictures/Screenshots/image-20260312093347563.png)

![image-20260312094230943](./../../../../Pictures/Screenshots/image-20260312094230943.png)

### 📋 核心任务文件

| 文件名                                                       | 用途                                               |
| ------------------------------------------------------------ | -------------------------------------------------- |
| [sentiment_analysis.py](sentiment_analysis.py)               | 核心情感分析代码，调用Deepseek API                 |
| [evaluate.py](evaluate.py)                                   | 评估模块，计算准确率                               |
| [data_with_prediction.csv](data_with_prediction.csv)         | 包含text、label、deepseek_prediction三列的最终数据 |
| [error_samples.csv](error_samples.csv)                       | 提取出的预测错误的样本                             |
| [data_with_optimized_prediction_v2.csv](data_with_optimized_prediction_v2.csv) | 优化prompt后的预测结果                             |
| [comparison_results_v2.json](comparison_results_v2.json)     | 优化前后准确率对比                                 |
| [optimized_prompt.txt](optimized_prompt.txt)                 | 优化后的prompt                                     |

- 最终准确率：93.33%（比原始提高11.67%）
import pandas as pd

file_path = "C:\\Users\\shizimu\\Desktop\\导师\\cancer patient data sets.csv"
df = pd.read_csv(file_path)


print("缺失值统计：")
print(df.isnull().sum())

df["Patient Id"] = df["Patient Id"].astype(str)


df["Age"] = pd.to_numeric(df["Age"], errors="coerce")  # 将错误值转换为 NaN
df.loc[~df["Age"].between(0, 120), "Age"] = None  # 过滤不合理年龄


df = df[df["Gender"].isin([0, 1])]


valid_levels = ["Low", "Medium", "High"]
df = df[df["Level"].isin(valid_levels)]

# 统计学描述，查找异常值
print("数据描述：")
print(df.describe())

# 检查 Patient Id 是否唯一
if df["Patient Id"].nunique() == len(df):
    print("Patient Id 唯一性检查通过 ✅")
else:
    print("Patient Id 存在重复 ❌")

# 8. 保存清理后的数据集
cleaned_file_path = "/mnt/data/cleaned_cancer_patient_data.csv"
df.to_csv(cleaned_file_path, index=False)
print(f"清理后的数据已保存至: {cleaned_file_path}")

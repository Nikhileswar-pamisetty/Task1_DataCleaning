import pandas as pd

# Load the dataset
df = pd.read_csv(r"C:\Users\dell\Desktop\Elevate labs\task1\task1 cleaned dataset.csv")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Rename columns to lowercase with underscores
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

df.rename(columns={'no-show': 'no_show'}, inplace=True)


# Standardize values
df['gender'] = df['gender'].str.upper().str.strip()
df['no_show'] = df['no_show'].str.upper().str.strip()

# Convert date columns to datetime
df['scheduledday'] = pd.to_datetime(df['scheduledday'], errors='coerce')
df['appointmentday'] = pd.to_datetime(df['appointmentday'], errors='coerce')
df['appointmentid'] = pd.to_numeric(df['appointmentid'], errors='coerce').fillna(0).astype(int)

df['patientid'] = df['patientid'].apply(lambda x: f"{float(x):.1f}" if pd.notnull(x) else '')



# Clean and fix age
df['age'] = pd.to_numeric(df['age'], errors='coerce').fillna(0).astype(int)
df = df[df['age'] >= 0]


# Assign correct data types
df['gender'] = df['gender'].astype('category')
df['neighbourhood'] = df['neighbourhood'].astype('category')
df['scholarship'] = df['scholarship'].astype(int)
df['hipertension'] = df['hipertension'].astype(int)
df['diabetes'] = df['diabetes'].astype(int)
df['alcoholism'] = df['alcoholism'].astype(int)
df['handcap'] = df['handcap'].astype(int)
df['sms_received'] = df['sms_received'].astype(int)
df['no_show'] = df['no_show'].astype('category')

# Save cleaned dataset
df.to_csv(r"C:\Users\dell\Desktop\Elevate labs\task1\task1 cleaned dataset.csv", index=False)

import pandas as pd

# Load the data from CSV files
file1 = pd.read_csv('Hotel Reservations_ZC.csv')
file2 = pd.read_csv('ZC_DATASET.csv')

# Map the is_canceled values in file1 to 0 and 1
file1['is_canceled'] = file1['is_canceled'].map({'Not_Canceled': 0, 'Canceled': 1})

# Merge the two dataframes on ID
merged = file1.merge(file2, on='ID', suffixes=('_file1', '_file2'))

# Find matches and mismatches
matches = merged[merged['is_canceled_file1'] == merged['is_canceled_file2']]
mismatches = merged[merged['is_canceled_file1'] != merged['is_canceled_file2']]

# Print the number of matches
print(f'Number of matches: {len(matches)}')

# Calculate the number of matches and mismatches out of file2
num_matches = len(matches)
num_mismatches = len(mismatches)
total_file2 = len(file2)

# Calculate the percentage of success
success_rate = (num_matches / total_file2) * 100
no_success_rate = 100 - success_rate

# Print the number of matches out of the total number of rows in file2
print(f'Number of matches: {num_matches} out of {total_file2}')
print(f'Success rate: {success_rate:.2f}%')
print(f'No Success rate: {no_success_rate:.2f}%')



# Print mismatches with their IDs and corresponding values
if not mismatches.empty:
    #print('Mismatches found:')
    for _, row in mismatches.iterrows():
        #print(f"ID: {row['ID']}, file1 value: {row['is_canceled_file1']}, file2 value: {row['is_canceled_file2']}")
        continue
else:
    print('No mismatches found.')

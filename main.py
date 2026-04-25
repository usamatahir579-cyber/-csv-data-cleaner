def clean_csv(input_file, output_file):
    seen_rows = set()

    with open(input_file, "r") as f, open(output_file, "w") as out:

        dirty_count = 0
        total_count = 0

        for line in f:
            total_count += 1

            parts = line.strip().split(",")

            if len(parts) != 3:
                continue

            name = parts[0].strip()
            age = parts[1].strip()
            salary = parts[2].strip()

            # fix missing / invalid age
            if age == "" or not age.isdigit():
                age = "0"
                dirty_count += 1

            # create cleaned row
            row = f"{name},{age},{salary}"

            # remove duplicates
            if row in seen_rows:
                continue

            seen_rows.add(row)

            out.write(row + "\n")

    print("Cleaning completed ✔")
    print("Total rows:", total_count)
    print("Dirty rows fixed:", dirty_count)
    print("Duplicates removed:", len(seen_rows))
    

clean_csv("data.csv", "cleaned_data.csv")
# List of Code Challenges

## Stage 2

- [x] 1. What is the line to import the built-in csv module?

    `import csv`

- [x] 2. Write a function `open_with_csv` that takes a string argument with the filename and default delimiter argument of a tab space. Your function will open filename with csv's reader function and return an empty list `data`that contains the csv file contents.

    ```
    def open_with_csv(filename, d='\t'):
        data = []
        with open(filename, encoding='utf-8') as tsvin:
            tsvin = csv.reader(tsvin, delimiter=d)
            for row in tsvin:
                data.append(row)
        return data
    ```

## Stage 3

- [x] 1. Filter all the DKNY branded ties from data_from_csv into a variable dkny_ties using the function shown in the video, filter_col_by_string()

    `dkny_ties = filter_col_by_string(data_from_csv, "brandName", "DKNY")`

- [x] 2. Filter all the solid color ties under $35 to the variable solid35 and over $45 to the variable solid45 using the function filter_col_by_float() and starting with the data, solid_ties. Assume that `solid_ties = filter_col_by_string(data_from_csv, "print", "_solid")` and `data_from_csv = open_with_csv("data.csv")`

    ```
    solid35 = filter_col_by_float(solid_ties, "priceLabel", "<", 35)
    solid45 = filter_col_by_float(solid_ties, "priceLabel", ">", 45)
    ```

- [x] 3. Is the average Gucci tie price higher than the average J. Crew tie price? Write a function `comparison()`` that compares Gucci tie price, `gucci_ties` and J.Crew Tie price, `jcrew_ties`. The comparison function will print out the one sentence "The brand that is more likely to have a higher price tag is: brandName" where brandName is the brand with a higher price.

    ```
    def comparison(brand_a, brand_a_avg, brand_b, brand_b_avg):
        brand_name = ""
        if float(brand_a_avg) > float(brand_b_avg):
            brand_name = brand_a
        elif float(brand_a_avg) < float(brand_b_avg):
            brand_name = brand_b
        else:
            brand_name = "neither"
        return "The brand that is more likely to have a higher price tag is: {}".format(brand_name)

    sentence = comparison("Gucci", avg_gucci, "J. Crew",  avg_jcrew)
    ```

- [ ] 4. *bonus* Write a function filter_by_brand_and_price(data, brand, price) that lets you filter a dataset with the two conditions. 

    ```
    def filter_by_brand_and_price(data_sample, brand, price):
        new_data = []

        #find index of field in the first row
        brand_index = 5
        price_index = 2

        new_data.append(data_sample[0])

        for row in data_sample[1:]:
            if row[brand_index] == brand:
                new_data.append([str(x).encode('utf8') for x in row])
            if row[price_index] == price:
                new_data.append([str(x).encode('utf8') for x in row])
                
        return new_data

    def write_brand_and_price_to_file(filename, data_sample):

        # confirm that the columns only have two columns, otherwise take the two fields
        num_fields = len(data_sample[0])
        
        brand_field_index = 5 #int(dataSample[0].index("brand"))
        price_field_index = 2 #int(dataSample[0].index("priceLabel"))
        
        #if numFields > 2:
        new_array = []
        for record in data_sample:
            new_record = [None] * 2
            new_record[0] = record[brand_field_index]
            new_record[1] = record[price_field_index]
            new_array.append(new_record)

        # write the file
        write_to_file(filename, new_array) 
    ```

## Stage 4

- [x] 1. Using the function, filter_col_by_string(), how would you call it so that it exports 'Dolce & Gabbana' brand ties?

    ```
    dolce_gabbana = filter_col_by_string(data_from_csv, "brandName", "Dolce & Gabbana")
    ```

- [ ] 2. Define a function that would allow you to filter ties made of 'cotton' material and a print matching the string "_striped". This would be a function that accepts two arguments and returns a list.  (rewrite may be needed)

    ```
    cotton = filter_col_by_string(data_from_csv, "material", "_cotton")
    striped = filter_col_by_string(cotton, "print", "_striped")

    def two_cols(data_sample, field1, field1_value, field2, field2_valu):
        filtered_rows = []
        
        #find index of field in the first row
        col1 = int(the_data[0].index(field1))
        col2 = int(the_data[0].index(field1))

        filtered_rows.append(data_sample[0])

        for row in data_sample[1:]:
            if row[col1] == field1_value:
                filtered_rows.append([str(x).encode('utf8') for x in row])
            if row[col2] == field2_value:
                filtered_rows.append([str(x).encode('utf8') for x in row])
                
        return filtered_rows
    ```

- [ ] 3. Define a function with two input arguments: (1) filename, and (2) a list of columns to be exported using integer values. (rewrite may be needed)

    ```
    def my_functon(filename, columns_list):
        filename=""
        columns_list=""
    ```

- [ ] 4. Export a CSV file with each sample having only three fields: brand name, price, and material. How would you call the function from task 3 that takes in two arguments? (rewrite may be needed)

    ```
    def write_brand_and_price_to_file(filename, data_sample):

        # confirm that the columns only have two columns, otherwise take the two fields
        num_fields = len(data_sample[0])
        
        brand_field_index = 5 
        price_field_index = 2 
        
        #if numFields > 2:
        new_array = []
        for record in data_sample:
            new_record = [None] * 2
            new_record[0] = record[brand_field_index]
            new_record[1] = record[price_field_index]
            new_array.append(new_record)

        # write the file
        write_to_file(filename, new_array) 

    my_function("x.csv", "brandName", "price", "material")
    ```

## Stage 5

- [x] 1. How would you create a new matplotlib figure with the pyplot module and set the chart to ggplot style? Hint: You'll want to import pyplot and use the figure function. 

    ```
    import matplotlib.pyplot as plt
    plt.style.use('ggplot') 
    fig = plt.figure() 
    ```

- [x] 2. Extract a data sample from `data_from_csv` of `cotton_ties` and from that, extract a data sample `cotton_and_striped` that has only ties made of cotton material and striped print using the function `filter_col_by_string()`. 

    ```
    cotton_ties = filter_col_by_string(data_from_csv, "material", "_cotton")
    cotton_and_striped = filter_col_by_string(cotton_ties, "print", "_striped")
    ```

- [x] 3. See the example code snippet displayed [above]. We want to plot the price of the cotton and striped ties cotton_and_striped on a bar chart and set the title variable to be ‘Cotton and Stripes’. We want one of the axis labels to indicate 'Prices', and another axis label to indicate 'Ties'. How would you fill in the strings that say 'FILL THIS IN' to properly label the chart?

    ```
    ax.set_title('Cotton and Stripes')
    ax.set_ylabel('Price')
    ax.set_xlabel('Ties')
    ```

## Stage 6

- [x] 1. What module would you have to import from matplotlib to create pdfs? Write the import statement.

    ```
    from matplotlib.backends.backend_pdf import PdfPages
    ```

- [x] 2. How would you create a pdf object?

    ```
    my_pdf = PdfPages('reports.pdf')
    ```

- [x] 3. What is the code to close a pdf object stream?

    ```
    my_pdf.close()
    ``` 

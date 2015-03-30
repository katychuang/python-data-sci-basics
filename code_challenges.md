# List of Code Challenges

## Stage 2

1. Try to import the csv module

    `import csv`

2. Write a function `open_with_csv` that takes one argument parameter. This function will return an empty list `data`.

    ```
    def open_with_csv(filename):
        data = []
        return data
    ```

## Stage 3

1. Filter all the DKNY branded ties from my_csv into dkny_ties using the function filter_col_by_string()

    `filter_col_by_string(data_from_csv, "brandName", "DKNY")`

2. Filter all the solid color ties under $35 to solid35 and over $45 to solid45 using the function filter_col_by_float() and starting with the data, data_from_csv. 

    ```
    solid_ties = filter_col_by_string(data_from_csv, "pattern", "_solid")
    solid35 = filter_col_by_float(solid_ties, "priceLabel", "<", 35)
    solid45 = filter_col_by_float(solid_ties, "priceLabel", ">", 45)
    ```

3. Is the average Gucci tie price higher than the average J. Crew tie price? Write a function comparison() that compares Gucci tie price and J.Crew Tie price, and prints out the one sentence "The brand that is more likely to have a higher price tag is: brandName" where brandName is the brand  with a higher price.

    ```
    def comparison(brand_a, brand_b):
        brand_name = ""
        if brand_a > brand_b:
            brand_name = brand_a
        elif brand_b > brand_a:
            brand_name = brand_b
        else:
            brand_name = "neither"
        return "The brand that is more likely to have a higher price tag is:{}".format(brand_name)

    comparison(gucci_ties, jcrew_ties)
    ```

4. *bonus* Write a function filter_by_brand_and_price(data, brand, price) that lets you filter a dataset with two conditions

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
    ```

## Stage 4

1. Using the function, filter_col_by_string(), how would you call it so that it exports 'Dolce & Gabbana' brand ties?

    ```
    dolce_gabbana = filter_col_by_string(data_from_csv, "brandName", "Dolce & Gabbana")
    ```

2. Define a function that would allow you to filter ties made of 'cotton' material and a pattern matching the string "_striped" under the striped field. This would be a function that accepts two arguments and returns a list.  (rewrite may be needed)

    ```
    cotton = filter_col_by_string(data_from_csv, "material", "cotton")
    striped = filter_col_by_string(cotton, "pattern", "_striped")

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

3. Define a function with two input arguments: (1) filename, and (2) a list of columns to be exported using integer values. (rewrite may be needed)

    ```
    def my_functon(filename, columns_list):
        filename=""
        columns_list=""
    ```

4. Export a CSV file with each sample having only three fields: brand name, price, and material. How would you call the function from task 3 that takes in two arguments? (rewrite may be needed)

    ```
    my_function("x.csv", "brandName", "price", "material")
    ```

## Stage 5

1. How would you create a new matplotlib figure with the pyplot module and set the chart to ggplot style? Hint: You'll want to import pyplot and use the figure function. 

    ```
    import matplotlib.pyplot as plt
    plt.style.use('ggplot') 
    fig = plt.figure() 
    ```

2. Create a data sample cotton_and_striped that has only ties made of cotton material and striped pattern using the function filter_col_by_string(). 

    ```
    cotton_ties = filter_col_by_string(my_data, "material", "cotton")
    cotton_and_striped = filter_col_by_string(cotton_ties, "pattern", "_striped")
    ```

3. Plot the cotton and striped ties cotton_and_striped on a bar chart and set the title variable to be ‘Cotton and Stripes’ (rewrite may be needed)

    ```

    ```

## Stage 6

1. What module would you have to import from matplotlib to create pdfs? Write the import statement.

    ```
    from matplotlib.backends.backend_pdf import PdfPages
    ```

2. How would you create a pdf object?

    ```
    my_pdf = PdfPages('reports.pdf')
    ```

3. What is the code to close a pdf object stream?

    ```
    my_pdf.close()
    ``` 

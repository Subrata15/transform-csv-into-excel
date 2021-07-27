'''
1. Commonly developers/DS used pandas to read, buat sometimes will appear problem in codec or another problem happened.
2. We need alternative way to transfor/converting csv file into excel, for any purpose used.
'''

# pip install jpype1
# pip install aspose-cells

def trans_cx(path, output_path, type_file_output='excel'):
    if type_file_output == 'excel':
        try:
            import pandas as pd
            df = pd.read_csv(path, error_bad_lines=True)
            df.to_excel(output_path, index=False)
            return 'Ok main'

        except:
            # Note: currently using asposecells will contain new sheet filled WARNING and Copyright statement
            import jpype
            import asposecells
            jpype.startJVM()
            from asposecells.api import Workbook, LoadOptions, SaveFormat, FileFormatType, SaveFormat

            # Create CSV LoadOptions object
            loadOptions =  LoadOptions(FileFormatType.CSV)

            # Create a Workbook object with CSV file's path and the loadOptions
            workbook =  Workbook(path, loadOptions)

            # Save CSV as XLSX
            workbook.save(output_path, SaveFormat.XLSX)

            return 'Ok alt'
    elif type_file_output == 'csv':
        import pandas as pd
        df = pd.read_excel(path)
        df.to_csv(output_path, index=False)
        return 'Ok main'
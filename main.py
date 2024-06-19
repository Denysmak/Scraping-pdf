import tabula
import os

def store_tables():
    pdf_path = 'extenso_documento_exemplo.pdf'

    dfs = tabula.read_pdf(pdf_path, pages='all')

    output_dir = 'csv files'

    os.makedirs(output_dir, exist_ok=True)

    for i, df in enumerate(dfs):
        output_file = os.path.join(output_dir, f'all_pages_table_{i}.csv')
        df.to_csv(output_file, index=False)
store_tables()




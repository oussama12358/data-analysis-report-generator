import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from openai import OpenAI
from fpdf import FPDF
import os

# ضع مفتاح API الخاص بك هنا
api_key = 'ضع_مفتاح_OpenAI_API_هنا'
client = OpenAI(api_key=api_key) if api_key != 'ضع_مفتاح_OpenAI_API_هنا' else None

def load_data(file_path):
    # Clean the file path by removing quotes, extra spaces, and command characters
    file_path = file_path.strip()
    # Remove command characters like & and quotes
    file_path = file_path.replace('&', '').strip()
    file_path = file_path.strip('"').strip("'").strip()
    
    # Get file extension
    file_extension = os.path.splitext(file_path)[1].lower()
    
    # Load data based on file type
    if file_extension == '.csv':
        return pd.read_csv(file_path)
    elif file_extension in ['.xlsx', '.xls']:
        return pd.read_excel(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_extension}. Supported formats: .csv, .xlsx, .xls")

def analyze_data(df):
    description = df.describe()
    return description

def create_chart(df, chart_file):
    # Set up the plot style
    try:
        plt.style.use('seaborn-v0_8')
    except:
        plt.style.use('default')
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Data Distribution Analysis', fontsize=20, fontweight='bold', color='#2c3e50')
    
    # Define colors
    colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']
    
    # Create histograms for each column
    columns = df.select_dtypes(include=[np.number]).columns
    for i, col in enumerate(columns):
        if i < 4:  # Limit to 4 subplots
            row = i // 2
            col_idx = i % 2
            ax = axes[row, col_idx]
            
            # Create histogram
            ax.hist(df[col], bins=8, color=colors[i], alpha=0.7, edgecolor='white', linewidth=2)
            ax.set_title(f'{col} Distribution', fontweight='bold', color='#2c3e50', fontsize=16)
            ax.set_xlabel(col, fontsize=14)
            ax.set_ylabel('Frequency', fontsize=14)
            ax.grid(True, alpha=0.3)
            
            # Make tick labels larger
            ax.tick_params(axis='both', which='major', labelsize=12)
            
            # Add statistics text
            mean_val = df[col].mean()
            std_val = df[col].std()
            ax.text(0.02, 0.98, f'Mean: {mean_val:.1f}\nStd: {std_val:.1f}', 
                   transform=ax.transAxes, verticalalignment='top',
                   bbox=dict(boxstyle='round', facecolor='white', alpha=0.8),
                   fontsize=12)
    
    # Hide unused subplots
    for i in range(len(columns), 4):
        row = i // 2
        col_idx = i % 2
        axes[row, col_idx].set_visible(False)
    
    plt.tight_layout()
    plt.savefig(chart_file, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def generate_summary(description):
    if client is None:
        return "Note: OpenAI API key not provided. Simple summary generated:\n\n" + description.to_string()
    
    try:
        prompt = f"Here are statistics from a dataset:\n{description.to_string()}\nPlease create a detailed and comprehensive summary in English with the following structure:\n1. Data Overview\n2. Key Insights\n3. Trends Analysis\n4. Recommendations\nMake it professional and easy to understand:"
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating summary with OpenAI: {str(e)}\n\nSimple summary:\n{description.to_string()}"

def generate_pdf(summary, chart_file, output_pdf):
    pdf = FPDF()
    pdf.add_page()
    
    # Set up colors
    pdf.set_draw_color(41, 128, 185)  # Blue border
    pdf.set_fill_color(52, 152, 219)  # Light blue background
    pdf.set_text_color(44, 62, 80)    # Dark blue text
    
    # Header with background
    pdf.set_font("Arial", "B", 24)
    pdf.cell(0, 18, "Data Analysis Report", 1, 1, "C", True)
    pdf.ln(12)
    
    # Summary section with styled background
    pdf.set_font("Arial", "B", 16)
    pdf.set_fill_color(236, 240, 241)  # Light gray background
    pdf.cell(0, 12, "Executive Summary", 1, 1, "L", True)
    pdf.ln(6)
    
    # Summary content
    pdf.set_font("Arial", size=13)
    pdf.set_text_color(44, 62, 80)
    
    # Clean up any remaining non-ASCII characters for PDF compatibility
    english_summary = summary
    
    # Remove any remaining Arabic characters that might cause issues
    import re
    english_summary = re.sub(r'[^\x00-\x7F]+', '', english_summary)
    
    # Simple text output
    pdf.multi_cell(0, 8, english_summary, 0, "L")
    
    pdf.ln(12)
    
    # Chart section header
    pdf.set_font("Arial", "B", 16)
    pdf.set_fill_color(236, 240, 241)
    pdf.cell(0, 12, "Data Visualization", 1, 1, "L", True)
    pdf.ln(6)
    
    # Add chart with border
    pdf.set_draw_color(189, 195, 199)
    pdf.rect(10, pdf.get_y(), 190, 120)
    pdf.image(chart_file, x=15, y=pdf.get_y() + 5, w=180)
    
    # Footer
    pdf.ln(130)
    pdf.set_font("Arial", "I", 10)
    pdf.set_text_color(127, 140, 141)
    pdf.cell(0, 6, "Generated by Data Analysis Tool", 0, 1, "C")
    
    pdf.output(output_pdf)

def main():
    print("=== Data Analysis Report Generator ===")
    print("Supported formats: CSV (.csv), Excel (.xlsx, .xls)")
    print("\nExamples:")
    print("  - test_data.csv")
    print("  - test_data.xlsx")
    print("  - sales_data.xlsx")
    print("  - C:\\Users\\username\\Desktop\\data.xlsx")
    print("\nAvailable test files in current directory:")
    print("  - test_data.csv")
    print("  - test_data.xlsx")
    file_path = input("\nEnter file path: ").strip()
    
    # Check if user entered anything
    if not file_path:
        print("Error: No file path entered. Please try again.")
        return
    
    try:
        df = load_data(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found. Please check the file path and try again.")
        return
    except ValueError as e:
        print(f"Error: {str(e)}")
        return
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return

    print("Analyzing data...")
    description = analyze_data(df)

    print("Creating chart...")
    
    # Create unique chart filename based on input file
    input_filename = os.path.splitext(os.path.basename(file_path))[0]
    chart_file = f"chart_{input_filename}.png"
    create_chart(df, chart_file)

    print("Generating summary using GPT...")
    summary = generate_summary(description)

    print("Creating PDF report...")
    
    # Create unique filename based on input file
    input_filename = os.path.splitext(os.path.basename(file_path))[0]
    output_pdf = f"report_{input_filename}.pdf"
    generate_pdf(summary, chart_file, output_pdf)

    print(f"Report created: {output_pdf}")

if __name__ == "__main__":
    main()

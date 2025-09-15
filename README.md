# 📊 Data Analysis Report Generator

A powerful tool for analyzing CSV and Excel files and generating professional PDF reports with AI-powered insights.

## ✨ Features

- **📁 Multiple File Support**: CSV (.csv), Excel (.xlsx, .xls)
- **🤖 AI-Powered Analysis**: OpenAI GPT-4 integration for intelligent insights
- **📈 Beautiful Visualizations**: Professional charts and graphs
- **📄 PDF Reports**: Styled, professional PDF reports
- **🌐 Web Interface**: Easy-to-use Streamlit web application
- **💻 Command Line**: Terminal-based version for automation

## 🚀 Quick Start

### Option 1: Web Application (Recommended)

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the web app:**
   ```bash
   streamlit run streamlit_app.py
   ```

3. **Open your browser:**
   ```
   http://localhost:8501
   ```

4. **Upload your file and generate reports!**

### Option 2: Command Line

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the script:**
   ```bash
   python report_generator.py
   ```

3. **Enter your file path when prompted**

## 📋 Supported File Formats

| Format | Extension | Description |
|--------|-----------|-------------|
| CSV | `.csv` | Comma-separated values |
| Excel | `.xlsx` | Excel 2007+ format |
| Excel | `.xls` | Excel 97-2003 format |

## 🔧 Configuration

### OpenAI API Key (Optional)

For AI-powered analysis, add your OpenAI API key:

1. **In the code files**, replace:
   ```python
   api_key = 'ضع_مفتاح_OpenAI_API_هنا'
   ```
   
2. **With your actual key:**
   ```python
   api_key = 'sk-your-actual-openai-key-here'
   ```

**Note:** Without an API key, the tool will generate basic statistical summaries.

## 📁 Data Analysis Report Generator

```
Data Analysis Report Generator/
├── streamlit_app.py          # Web application (Streamlit)
├── report_generator.py       # Command-line version
├── requirements.txt          # Python dependencies
├── README.md                # This file
├── test_data.csv            # Sample CSV file
└── test_data.xlsx           # Sample Excel file
```

## 🌐 Deployment

### Vercel Deployment

1. **Push to GitHub**
2. **Connect to Vercel**
3. **Deploy automatically**

### Local Development

```bash
# Clone the repository
git clone <your-repo-url>
cd project-freelance

# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run streamlit_app.py
```

## 📊 Sample Output

The tool generates:
- **Data Preview**: First 10 rows of your data
- **Statistics**: Comprehensive statistical analysis
- **Visualizations**: Beautiful charts and graphs
- **AI Summary**: Intelligent insights and recommendations
- **PDF Report**: Professional, downloadable report

## 🛠️ Dependencies

- **streamlit**: Web application framework
- **pandas**: Data manipulation and analysis
- **matplotlib**: Data visualization
- **numpy**: Numerical computing
- **openai**: AI integration
- **fpdf2**: PDF generation
- **openpyxl**: Excel file support

## 📝 Usage Examples

### Web Interface
1. Upload your CSV/Excel file
2. View data preview and statistics
3. See beautiful visualizations
4. Read AI-generated insights
5. Download professional PDF report

### Command Line
```bash
python report_generator.py
# Enter file path: data/sales_data.xlsx
# Report created: report_sales_data.pdf
```

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This project is open source and available under the MIT License.

---

**Made with ❤️ for data analysis enthusiasts!**

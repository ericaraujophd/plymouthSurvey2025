# Plymouth Heights CRC Survey Analysis Project

## Overview

This project analyzes congregational survey responses for Plymouth Heights CRC to guide the completion of their church profile form for the pastoral search process. The analysis combines quantitative statistical methods and qualitative text analysis to extract meaningful insights from 68 survey responses.

## Project Structure

```
search-report/
├── README.md                           # This file
├── context.txt                         # Project background and goals
├── requirements.txt                    # Python dependencies
├── church-profile-form.md              # Template form (DO NOT MODIFY)
├── survey-answers.csv                  # Survey data (DO NOT MODIFY)
├── venv/                               # Python virtual environment
├── analysis/                           # Analysis scripts
│   ├── data_analysis.py                # Quantitative analysis
│   └── text_analysis.py                # Qualitative text analysis
└── outputs/                            # Generated reports and visualizations
    ├── analysis_report.md              # Comprehensive analysis report
    ├── profile_guidance.md             # Church profile form completion guide
    └── figures/                        # 16 data visualizations
        ├── attendance_frequency.png
        ├── scale_questions.png
        ├── ministry_participation.png
        ├── church_strengths.png
        ├── cultural_challenges.png
        └── [11 word clouds]
```

## Key Deliverables

### 1. Comprehensive Analysis Report ([outputs/analysis_report.md](outputs/analysis_report.md))
A detailed 12-section report covering:
- Executive summary with key findings
- Worship and service characteristics
- Ministry participation and discipleship
- Belonging and community integration
- Community outreach and mission
- Church strengths and identity
- Cultural challenges and denominational identity
- Goals for next 3-5 years
- Pastor search priorities and qualities
- Statistical summaries
- Red flags and recommendations

### 2. Profile Form Guidance ([outputs/profile_guidance.md](outputs/profile_guidance.md))
Section-by-section recommendations for completing the church profile form, including:
- Data-driven responses for each form section
- Supporting evidence from survey
- Multiple-choice selections with rationale
- Narrative response templates
- Interview questions for candidates
- Red flags and green flags to watch for

### 3. Data Visualizations ([outputs/figures/](outputs/figures/))
16 professional visualizations including:
- Bar charts for categorical data
- Distribution charts for scale questions
- Word clouds for open-ended responses
- Horizontal bar charts for rankings

## Key Findings

### Demographics
- **68 total responses**
- **94% weekly attenders** (very high commitment)
- **88% involved beyond Sunday worship**

### Worship Preferences
- **Music style:** Strong preference for blended (mean: 2.91/5, where 3 = balanced)
- **54% chose perfectly balanced** worship music
- **Member involvement:** Current level viewed as appropriate (mean: 2.82/5)

### Top Church Strengths
1. **Worship services** (68%)
2. **Community presence** (47%)
3. **Youth program ministries** (46%)
4. **Value for diversity** (44%)
5. **Leadership** (29%)

### Primary Challenges
1. **Nurturing young people** (69% - top challenge)
2. **Busy lives/competing priorities** (59%)
3. **Welcoming community members** (35%)
4. **Gender identification issues** (19%)

### Pastor Priorities (First Year)
1. **Fostering belonging** (31% mentioned)
2. **Strong biblical preaching** (19%)
3. **Youth programs** (18%)
4. **Getting to know congregation** (16%)
5. **Community engagement** (15%)

### Essential Pastor Qualities
1. **Exceptional preaching** (most cited - non-negotiable)
2. **Relational/people skills**
3. **Strong leadership capabilities**
4. **Long-term commitment**
5. **Community engagement passion**

### CRC Relationship
- **Mixed sentiment** - ranges from very positive to critical
- **Tension around** human sexuality positions and synodical decisions
- **Need for pastor** who can navigate theological diversity with grace

## Running the Analysis

### Prerequisites
- Python 3.8+
- Virtual environment (included)

### Setup
```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies (if needed)
pip install -r requirements.txt
```

### Run Analysis
```bash
# Quantitative analysis
python analysis/data_analysis.py

# Text analysis
python analysis/text_analysis.py
```

### Output
- Console output with statistical summaries
- Visualizations saved to `outputs/figures/`
- Reports already generated in `outputs/`

## Analysis Methods

### Quantitative Analysis
- **Descriptive statistics** (mean, median, std dev) for scale questions
- **Frequency distributions** for categorical responses
- **Bar charts and histograms** for visualization
- **Multiple choice parsing** with semicolon-separated values

### Qualitative Analysis
- **Keyword extraction** using NLTK tokenization
- **Stop word filtering** (custom church context)
- **Word frequency analysis**
- **Word cloud generation** for thematic visualization
- **Manual thematic coding** of open-ended responses

### Tools Used
- **pandas** - Data manipulation and analysis
- **matplotlib/seaborn** - Statistical visualizations
- **NLTK** - Natural language processing
- **wordcloud** - Word cloud generation

## Important Notes

### Source Documents (DO NOT MODIFY)
- `church-profile-form.md` - Official template
- `survey-answers.csv` - Raw survey data
- These files should never be altered per project requirements

### Data Privacy
- Survey responses are de-identified (ID numbers only)
- No personally identifiable information in analysis
- Quotes used are representative samples without attribution

### Limitations
- **Survey bias:** 94% weekly attenders may not represent occasional attenders
- **Self-selection:** Those who completed survey may be more engaged
- **Demographics:** Survey didn't collect age/tenure data directly
- **Financial data:** Survey didn't address budget/compensation questions

### Recommendations for Committee
1. **Read the full analysis report** before completing profile form
2. **Review all visualizations** for pattern recognition
3. **Use profile guidance** as starting point, not final answer
4. **Supplement with** church records for missing data (demographics, financials)
5. **Confirm findings** with council/leadership discussions
6. **Be honest** about challenges while highlighting strengths

## Next Steps for Search Committee

1. ✅ Review comprehensive analysis report
2. ✅ Examine all data visualizations
3. ⬜ Complete profile form using guidance document
4. ⬜ Gather missing data from church records (demographics, financials, facilities)
5. ⬜ Draft narrative responses using templates provided
6. ⬜ Review completed profile with council for accuracy
7. ⬜ Finalize profile for submission to pastoral search coordinator
8. ⬜ Use interview questions provided when meeting candidates

## Questions or Issues?

This analysis provides the congregation's voice clearly. Combine this with:
- Leadership wisdom and discernment
- Church historical knowledge
- Financial and demographic records
- Prayer and seeking God's direction

The goal is a complete, honest, data-informed church profile that helps attract the right pastoral candidate for Plymouth Heights CRC's next season of ministry.

---

**Analysis Date:** December 2025
**Analyst:** Survey Analysis Team
**Survey Responses:** 68
**Response Rate:** Very Strong

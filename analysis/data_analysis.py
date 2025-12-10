"""
Main data analysis script for Plymouth Heights CRC survey responses
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re

# Set style for visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

def load_survey_data(filepath):
    """Load and perform initial exploration of survey data"""
    df = pd.read_csv(filepath)

    print("=" * 80)
    print("SURVEY DATA OVERVIEW")
    print("=" * 80)
    print(f"\nTotal responses: {len(df)}")
    print(f"Total questions: {len(df.columns)}")
    print(f"\nColumn names:")
    for i, col in enumerate(df.columns, 1):
        print(f"{i}. {col[:80]}...")

    return df

def analyze_attendance(df):
    """Analyze worship attendance patterns"""
    col = "How often do you typically attend Sunday worship services?"
    attendance = df[col].value_counts()

    print("\n" + "=" * 80)
    print("WORSHIP ATTENDANCE")
    print("=" * 80)
    print(attendance)

    # Create visualization
    plt.figure(figsize=(10, 6))
    attendance.plot(kind='bar', color='steelblue')
    plt.title('Worship Attendance Frequency', fontsize=16, fontweight='bold')
    plt.xlabel('Frequency', fontsize=12)
    plt.ylabel('Number of Respondents', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('outputs/figures/attendance_frequency.png', dpi=300, bbox_inches='tight')
    plt.close()

    return attendance

def analyze_scale_questions(df):
    """Analyze Likert scale questions (1-5 ratings)"""
    scale_questions = {
        'music_preference': "What proportion of traditional vs. contemporary music would you ideally prefer in our worship services? Consider 1 as totally traditional and 5 totally contemporary.",
        'member_involvement': "How would you describe the current level of member involvement in planning and participating in liturgy/worship? Consider 1 as no involvement at all and 5 as too much.",
        'missional_balance': 'Do you feel our missional focus is adequately balanced between "local and global" efforts? Consider 1 as not balanced at all and 5 totally balanced.',
    }

    results = {}

    print("\n" + "=" * 80)
    print("SCALE QUESTION ANALYSIS (1-5 Ratings)")
    print("=" * 80)

    for key, question in scale_questions.items():
        if question in df.columns:
            data = pd.to_numeric(df[question], errors='coerce').dropna()
            results[key] = {
                'mean': data.mean(),
                'median': data.median(),
                'std': data.std(),
                'distribution': data.value_counts().sort_index()
            }

            print(f"\n{key.upper().replace('_', ' ')}:")
            print(f"Mean: {results[key]['mean']:.2f}")
            print(f"Median: {results[key]['median']:.1f}")
            print(f"Std Dev: {results[key]['std']:.2f}")
            print("\nDistribution:")
            print(results[key]['distribution'])

    # Visualize scale questions
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    for idx, (key, question) in enumerate(scale_questions.items()):
        if question in df.columns:
            data = pd.to_numeric(df[question], errors='coerce').dropna()
            dist = data.value_counts().sort_index()

            axes[idx].bar(dist.index, dist.values, color='steelblue', alpha=0.7)
            axes[idx].axvline(data.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {data.mean():.2f}')
            axes[idx].set_xlabel('Rating', fontsize=10)
            axes[idx].set_ylabel('Count', fontsize=10)
            axes[idx].set_title(key.replace('_', ' ').title(), fontsize=12, fontweight='bold')
            axes[idx].legend()
            axes[idx].set_xticks([1, 2, 3, 4, 5])

    plt.tight_layout()
    plt.savefig('outputs/figures/scale_questions.png', dpi=300, bbox_inches='tight')
    plt.close()

    return results

def analyze_ministries_participation(df):
    """Analyze which ministries people participate in"""
    col = 'Beyond Sunday worship, in which PHCRC ministries or groups do you regularly participate?'

    # Parse semicolon-separated responses
    all_ministries = []
    for response in df[col].dropna():
        ministries = [m.strip() for m in str(response).split(';') if m.strip()]
        all_ministries.extend(ministries)

    ministry_counts = Counter(all_ministries)

    print("\n" + "=" * 80)
    print("MINISTRY PARTICIPATION")
    print("=" * 80)
    for ministry, count in ministry_counts.most_common():
        print(f"{ministry}: {count}")

    # Visualize top ministries
    top_ministries = dict(ministry_counts.most_common(10))
    plt.figure(figsize=(12, 6))
    plt.barh(list(top_ministries.keys()), list(top_ministries.values()), color='steelblue')
    plt.xlabel('Number of Participants', fontsize=12)
    plt.title('Top 10 Ministry Participation', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('outputs/figures/ministry_participation.png', dpi=300, bbox_inches='tight')
    plt.close()

    return ministry_counts

def analyze_church_strengths(df):
    """Analyze what people see as church strengths"""
    col = "From your perspective, what are PHCRC's greatest strengths or gifts as a church today? "

    # Parse multiple choice responses
    all_strengths = []
    for response in df[col].dropna():
        strengths = [s.strip() for s in str(response).split(';') if s.strip()]
        all_strengths.extend(strengths)

    strength_counts = Counter(all_strengths)

    print("\n" + "=" * 80)
    print("CHURCH STRENGTHS")
    print("=" * 80)
    for strength, count in strength_counts.most_common():
        print(f"{strength}: {count}")

    # Visualize
    plt.figure(figsize=(12, 6))
    strengths_dict = dict(strength_counts.most_common())
    plt.barh(list(strengths_dict.keys()), list(strengths_dict.values()), color='forestgreen')
    plt.xlabel('Number of Mentions', fontsize=12)
    plt.title("Church's Greatest Strengths", fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('outputs/figures/church_strengths.png', dpi=300, bbox_inches='tight')
    plt.close()

    return strength_counts

def analyze_cultural_challenges(df):
    """Analyze perceived cultural challenges"""
    col = "Which of the cultural challenges listed below do you feel are most pressing for PHCRC, and how can a new pastor help us navigate them?"

    all_challenges = []
    for response in df[col].dropna():
        challenges = [c.strip() for c in str(response).split(';') if c.strip()]
        all_challenges.extend(challenges)

    challenge_counts = Counter(all_challenges)

    print("\n" + "=" * 80)
    print("CULTURAL CHALLENGES")
    print("=" * 80)
    for challenge, count in challenge_counts.most_common():
        print(f"{challenge}: {count}")

    # Visualize
    plt.figure(figsize=(14, 8))
    challenges_dict = dict(challenge_counts.most_common())
    plt.barh(list(challenges_dict.keys()), list(challenges_dict.values()), color='coral')
    plt.xlabel('Number of Mentions', fontsize=12)
    plt.title('Most Pressing Cultural Challenges', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('outputs/figures/cultural_challenges.png', dpi=300, bbox_inches='tight')
    plt.close()

    return challenge_counts

def analyze_diversity_perceptions(df):
    """Analyze perceptions about welcoming and diversity"""
    col = "Thinking about PHCRC's challenges with welcoming new members, bridging age gaps, and embracing diverse families and backgrounds, which of the following best reflects your perception?"

    all_perceptions = []
    for response in df[col].dropna():
        perceptions = [p.strip() for p in str(response).split(';') if p.strip()]
        all_perceptions.extend(perceptions)

    perception_counts = Counter(all_perceptions)

    print("\n" + "=" * 80)
    print("DIVERSITY & WELCOMING PERCEPTIONS")
    print("=" * 80)
    for perception, count in perception_counts.most_common():
        print(f"{perception}: {count}")

    return perception_counts

def main():
    """Main analysis function"""
    print("\n" + "=" * 80)
    print("PLYMOUTH HEIGHTS CRC SURVEY ANALYSIS")
    print("=" * 80)

    # Load data
    df = load_survey_data('survey-answers.csv')

    # Run analyses
    attendance = analyze_attendance(df)
    scale_results = analyze_scale_questions(df)
    ministries = analyze_ministries_participation(df)
    strengths = analyze_church_strengths(df)
    challenges = analyze_cultural_challenges(df)
    perceptions = analyze_diversity_perceptions(df)

    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETE - Visualizations saved to outputs/figures/")
    print("=" * 80)

if __name__ == "__main__":
    main()

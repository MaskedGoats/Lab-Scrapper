import requests
from bs4 import BeautifulSoup
import gender_guesser.detector as gender_detector


def lab_names_url(url):    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    professor_name_elements = soup.find_all('a', href=True, target='_blank')
    #extract the names from the text you just collected
    lab_names = [elemnt.text.strip() for elemnt in professor_name_elements]
    return lab_names

def gender_ratio(names):
    gd = gender_detector.Detector()
    male = 0
    female = 0
    total = len(names)
    # look at first name and see if its male or female 
    for name in names:
        name_parts = name.split()
        if len(name_parts) > 0:
            first_name = name_parts[0]
            gender = gd.get_gender(first_name)
        
        if gender.startswith('m'):
            male = male + 1
        elif gender.startswith('f'):
            female = female + 1
    ratio_female = female/total
    ratio_male = male/total
    return male, female, total, ratio_female, ratio_male
    print(total)
if __name__ == '__main__':
    url = 'https://med.stanford.edu/neurology/faculty/overview.html'
    lab_names = lab_names_url(url)
    if lab_names:
        male, female, total, ratio_female, ratio_male = gender_ratio(lab_names)
        
        print(f"Total Labs: {total}")
        print(f"Number of male professors: {male}")
        print(f"Number of female professors: {female}")
        print(f"Percentage of female professors in neurology: {ratio_female*100:.2f}%")
        print(f"Percentage of male professors in neurology: {ratio_male*100:.2f}%")
    else:
        print("No lab names were found on the page.")
            
            
        
# BMI Calculator

This is a simple BMI (Body Mass Index) calculator implemented in Python.

## Author

Made by **Mohamed Elsayed**

## Description

This program calculates your BMI based on your weight and height, and categorizes it into different levels:

- Underweight
- Normal weight
- Overweight
- Obesity

My program is based on this BMI Datasheet: [BMI Datasheet](https://mohamed1242012.github.io/bmi_datasheet).

## Usage

Make sure python is installed :
- Debian: `sudo apt install python3`
- Arch: `sudo pacman -Sy python3`

Then clone my repo :
```bash
git clone https://github.com/Mohamed1242012/BMI-calc.git
cd BMI-calc
```

Then run the app :
```bash
python3 main.py
```

Choose wich units you want to use (Type 1 or 2) :
```bash
Which units do you prefer (1 or 2) :
1. Kilograms and Centimeters
2. Pounds and Inches (Feet + remaining inches)
Choose:
```
Then enter your weight and height.

## Future Updates
These are some things I want to add in the future :
1- GUI using tinker or pygtk
2- Make it support more units

## Datasheet :
### **BMI Calculation and Interpretation Datasheet**

#### **1. BMI Calculation Formula**
- **Formula:** 
  text{BMI} = \frac{\text{Weight (kg)}}{\text{Height (m)}^2}

#### **2. Units Conversion**
- **Height Conversion:**
  - From cm to m: 
    BMI = Weight (kg) / (Height (m) × Height (m))
- **Weight Conversion:**
  - From lbs to kg: 
    Weight (kg) = Weight (lbs) / 2.205

#### **3. BMI Categories and Interpretations**
| BMI Range | Category          | Interpretation |
|-----------|-------------------|----------------|
| < 18.5    | Underweight       | Increased risk for nutritional deficiencies |
| 18.5 - 24.9 | Normal weight    | Optimal health; lower risk for chronic diseases |
| 25.0 - 29.9 | Overweight       | Higher risk for chronic diseases; may need lifestyle changes |
| ≥ 30.0    | Obesity           | Significant risk for various health conditions |

#### **4. Age Considerations**
- **Children & Adolescents (2-19 years):**
  - Use BMI percentiles:
    - < 5th percentile: Underweight
    - 5th to 84th percentile: Healthy weight
    - 85th to 94th percentile: Overweight
    - ≥ 95th percentile: Obesity
- **Older Adults:**
  - BMI may underestimate body fat.
  - Consider body fat percentage and waist circumference for assessment.

#### **5. Gender Differences**
- **Body Composition:**
  - Men: Higher muscle mass, lower body fat.
  - Women: Higher body fat percentage.
- **Health Risks:**
  - Health implications of BMI categories may vary between genders.

#### **6. Additional Measurements for Health Assessment**
| Measurement              | Description                                  | Risk Thresholds           |
|-------------------------|----------------------------------------------|---------------------------|
| **Waist Circumference** | Indicates fat distribution                   | Men: > 102 cm (40 in) <br> Women: > 88 cm (35 in) |
| **Body Fat Percentage**  | Direct measure of body fat levels           | Varies by age and gender; consult health guidelines |

#### **7. Practical Application**
- **Children:** Use growth charts for BMI-for-age assessment.
- **Adults:** Combine BMI with waist circumference and body fat percentage for a comprehensive assessment.
- **Older Adults:** Discuss BMI with healthcare providers, considering changes in body composition.

## Licence
For licence info check the [LICENCE](LICENSE) file.

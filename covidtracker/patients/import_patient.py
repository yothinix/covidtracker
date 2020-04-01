from patients.models import Patient


def create_patient(name, age, email, is_positive, detail):
    patient = Patient.objects.create(
        name=name,
        age=age,
        email=email,
        is_positive=is_positive,
        detail=detail
    )

    print(f"created {patient}")


def run_import():
    patient_list = [
        ['Banana apple', 12, 'banana@apple.com', True, ''],
        ['Banana apple', 12, 'banana@apple.com', True, ''],
        ['Banana apple', 12, 'banana@apple.com', True, ''],
        ['Banana apple', 12, 'banana@apple.com', True, ''],
        ['Banana apple', 12, 'banana@apple.com', True, ''],
    ]

    for patient in patient_list:
        create_patient(patient[0], patient[1], patient[2], patient[3], patient[4])

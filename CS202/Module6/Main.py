from Patient import Patient
from Procedure import Procedure

def main():

    # The patient information
    patient = Patient('Isaiah', 'Luis', 'Rodriguez', 'Bobert Hospital', 'Seattle', 'WA', '99871', '888-300-2020', 'Dr. Elson', '509-312-2280')

    print(f'Patient information:\n{patient}\n')

    # The 3 procedures
    firstProcedure = Procedure('Physical Exam', 'May 14th 2024', 'Dr. Irvine', 250.00)
    print(f'Procedure #1:\n{firstProcedure}\n')
    
    secondProcedure = Procedure('X-ray', 'May 14th 2024', 'Dr. Jamison', 500.00)
    print(f'Procedure #2:\n{secondProcedure}\n')

    thirdProcedure = Procedure('Blood test', 'May 14th 2024', 'Dr. Smith', 200.00)
    print(f'Procedure #3:\n{thirdProcedure}\n')

    # The 3 accumulated costs from the 3 procedures
    totalcost = firstProcedure.cost + secondProcedure.cost + thirdProcedure.cost
    print(f'Total cost of all 3 procedures: ${totalcost:.2f}')

if __name__ == "__main__":
    main()
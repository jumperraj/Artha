import csv
from faker import Faker
from randomDT import random_date
import datetime


def data_gen(records, headers):
    fake = Faker('en_US')
    with open("abhi4.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):
            d1 = datetime.datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
            d2 = datetime.datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')
            writer.writerow({
                "Amount": fake.pyfloat(left_digits=8, right_digits=2, positive=True, min_value=10000, max_value=100000),
                "Sender_name": fake.name(),
                "repayment": fake.pyfloat(left_digits=8, right_digits=2, positive=True, min_value=100, max_value=1000),
                "Transaction ID": fake.pyint(min_value=3999, max_value=9999, step=1),
                "Date-Time": random_date(d1, d2),
            })


print("s001")
if __name__ == '__main__':
    records = 100
    headers = ["Amount", "Sender_name","Transaction ID", "repayment", "Date-Time"]
    data_gen(records, headers)
    print("CSV generation complete!")
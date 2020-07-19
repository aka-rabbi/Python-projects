#!/usr/bin/env python3

import json
import locale
import sys
from reports import generate as report_create
from emails import generate as email_generate,send


def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  locale.setlocale(locale.LC_ALL, 'en_US.UTF8')       #fixes locale so that json can be decoded in that format
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  #locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
  max_revenue = {"revenue": 0}
  max_sales = {'total_sales':0}
  most_popular = {}
  max_val =(0,0)
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    year_made = item['car']['car_year']
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    if item['total_sales']>max_sales['total_sales']:
      max_sales = item
    if year_made in most_popular:
      most_popular[year_made] += item['total_sales']
    else:
      most_popular[year_made] = item['total_sales']
  for key,val in most_popular.items():
    if val>max_val[1]:
      max_val = (key,val)
    

  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
      "The {} generated the most sales: {}".format(
      format_car(max_sales["car"]), max_sales["total_sales"]),
      "The most popular year was {} with {} sales.".format(
        max_val[0],max_val[1]),
  ]

  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("<>/car_sales.json")
  table_data = cars_dict_to_table(data)
  summary = process_data(data)
  print(summary)
  
  report_create('<>cars.pdf','Sales summary for last month',('<br/>').join(summary),table_data)
  
  #message = email_generate('automation@example.com','<user>@example.com','Sales summary for last month',('\n').join(summary),'/Users/aka/Documents/cars.pdf')
  #send(message)

if __name__ == "__main__":
  main(sys.argv)
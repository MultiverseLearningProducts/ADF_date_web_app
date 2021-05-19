# import libraries
import streamlit as st
from datecalc import duration, when

# select widescreen layout and elect page title
st.set_page_config(page_title='Date Calculator', layout='wide')

# print page title
st.title("Date Calculator")

#split into two columns
col1, col2 = st.beta_columns(2)

# create difference calculator
start_date = col1.date_input('Day 1')
end_date = col1.date_input('Day 2')

diff = duration(start_date, end_date)

col1.markdown(f'The difference is {diff} days!')

# create 'when' calculator
start_date2 = col2.date_input('Start Date')
duration = col2.number_input('Duration', min_value=0, max_value=1000000000, step=1)

end_date2 = when(start_date2, duration)

# reformat date
end_date2 = end_date2.strftime('%d %b %Y')

col2.markdown(f'{duration} days after your start date, it will be {end_date2}')
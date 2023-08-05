#!/usr/bin/bash

#ps -a |grep streamlit && /home/rome/.local/bin/streamlit run /home/rome/rrshare/rrshare/rqWeb/stock_RS_OH_MA_to_streamlit.py 

ps -a |grep streamlit
if [ $? -eq 0 ]; then
  echo "streamlit is already runned"
else
 # pkill -9 streamlit && 
streamlit run ~/rrshare/rrshare/rqWeb/stock_RS_OH_MA_to_streamlit.py
fi







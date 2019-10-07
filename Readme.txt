Prerequisites
    1.Python 3
    2. Flask


Working
    1. Linux
        1. Install flask using sudo apt install python3-flask
        2. open bash terminal in ooad folder and type "source setup.sh" without quotes .
        3. Server starts and do visit (your ip address):5000/startj
        4 .(Troubleshoot) If pip has issues , change pip to pip3 in setup.sh

    2. IDE like Pycharm
        1. Add this code at the end of main.py file to run within Pycharm
            if __name__=="__main__":
                app.run(host='0.0.0.0')
        2.Install flask in pycharm from file>>settings>>project Udaanhome >> python interpretor and clicking on "+" right side by searching 



## RPA Labs Solution
This is a solution to the problem defined by RPA Labs as indicated in file [problem.md](problem.md).

## ⚙ Usage
1. Clone the repository.
```bash
git clone https://github.com/SrjPdl/RPA-Labs-Solution.git
```
2. Install the dependencies.
```bash
pip install -r requirements.txt
```
If `pip` doesn't work use `pip3` instead of `pip`.

3. Run the application after changing current directory to app directory.
```bash
python3 manage.py runserver
```
If `python3` doesn't work use `python` instead of `python3`.

## Testing endpoints
There are mainly three endpoints which are implemented namely `/upload`, `/videos` and `/compute`.

#### Testing `/upload` endpoint
After running the application, go to `http://127.0.0.1:8000/upload` and upload a video file.

#### Testing `/videos` endpoint
After running the application, go to `http://127.0.0.1:8000/videos` and see the list of all uploaded videos.

To test several different filters, you can use the following query parameters as shown below:
```
http://127.0.0.1:8000/videos?<query1>=<value1>&<query2>=<value2>&<query3>=<value3>
```

where `<query>` is the name of the query parameter and `<value>` is the value of the query parameter.

`<query>` can be one of the following:
1. date - The date on which the video was uploaded in form `YYYY-MM-DD`.
2. size - The size of the video in MB.
3. minsize - The minimum size of the video in MB.
4. maxsize - The maximum size of the video in MB.
5. length - The length of the video in minutes.
6. minlength - The minimum length of the video in minutes.
7. maxlength - The maximum length of the video in minutes.
8. title - The title of the video. 

Example:
```
http://127.0.0.1:8000/videos?date=2022-07-20&minsize=3
```
#### Testing `/compute` endpoint
After running the application, go to `http://127.0.0.1:8000/compute` to compute the charges for the video after the validation.

## 🚀Author
Suraj Poudel



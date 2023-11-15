
https://www.kaggle.com/datasets/zsinghrahulk/crypto-currency-bitcoin-and-ethereum-data/download?datasetVersionNumber=1
This data set displays the pricing of Bitcoin and Eth with respect to daily categories of "Open" "high" "low" "Close" and "Volume".
Could use this dataset to see what time of year the Crypto market tends to be at its lowest and highest.

               Open          High           Low         Close     Adj Close        Volume
count   3654.000000   3654.000000   3654.000000   3654.000000   3654.000000  3.654000e+03
mean   12489.722362  12779.702503  12176.712024  12497.298504  12497.298504  2.132673e+10
std    15981.149824  16367.131613  15548.523408  15982.555689  15982.555689  1.657009e+10
min       84.279694     85.342743     82.829887     84.308296     84.308296  1.496177e+09
25%     1318.626008   1346.194641   1275.408967   1320.796630   1320.796630  9.610954e+09
50%     3880.535767   3964.966553   3783.871582   3881.728149   3881.728149  1.741543e+10
75%    20589.010253  21038.371580  20185.608885  20598.490722  20598.490722  2.857312e+10
max    67549.734380  68789.625000  66382.062500  67566.828130  67566.828130  3.509680e+11

https://www.kaggle.com/datasets/ishmaelkiptoo/motor-vehicle-collisions/download?datasetVersionNumber=1
Motor vehicle colosions in the state of New York with the collumns "CRASH DATE", "CRASH TIME", "ZIP CODE", and "LOCATION"
. If we wanted to dig deeper we could find some of the areas with most frequency of accidents. As well as the time of year where the most accidents happen.

CRASH DATE CRASH TIME   ZIP CODE    LOCATION
count      2034018    2034018  1400990.0     1803134
unique        4122       1440      426.0      276625
top     01/21/2014      16:00    11207.0  (0.0, 0.0)
freq          1161      28088    20041.0        4272

https://data.lacity.org/api/views/2nrs-mtv8/rows.csv?accessType=DOWNLOAD
Data set which reviews the crime that occurs in LA City. Filtered the collumns to only show  "Date Rptd" "AREA NAME" "Vict Sex".
This interestingly shows the most dangerous area based on # of reported crimes and also shows that most of the victims are reportedly male.


                     Date Rptd AREA NAME Vict Sex
count                   834319    834319   724431
unique                    1406        21        5
top     02/03/2023 12:00:00 AM   Central        M
freq                       924     56268   344140
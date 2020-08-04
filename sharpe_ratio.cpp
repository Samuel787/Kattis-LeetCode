#include <bits/stdc++.h>
using namespace std;

/**
 * @return standard deviation of the opening prices
 */
double calcSD(vector<double> prices){
    double mean = 0;
    for(double price: prices){
        mean += price;
    }
    mean /= prices.size();

    double E = 0;
    for(double price : prices){
        E += pow((price - mean), 2);
    }

    return sqrt(1.0/(prices.size() -1 ) * E);
}

/**
 * Returns from the naive trading strategy
*/
double calcPortfolioReturn(vector<double> prices){
    //employ the naive strategy
    double profit = 0;
    double window_avg = 0;
    bool has_stock = false;
    for(int i = 0; i <prices.size(); i++){
        if(i < 4){
            window_avg += prices[i];
        } else {
            if(i - 5 < 0){
                window_avg += prices[i];
                window_avg /= 5;
            } else {
                window_avg *= 5;
                window_avg -= prices[i - 5];
                window_avg += prices[i];
                window_avg /= 5;
            }
            // start trading
            if(prices[i] < window_avg && !has_stock){
                //buy stock
                has_stock = true;
                profit -= prices[i];
                cout << "profit changed buy: " << profit << endl;
            } 
            if(prices[i] > window_avg && has_stock){
                //sell stock
                has_stock = false;
                profit += prices[i];
                cout << "profit changed sell: " << profit << endl;
            }
        }
    }

    //sell away the stock one last time if have
    if(has_stock && prices.size() >= 5){
        profit += prices[prices.size() - 1];
        cout << "profit changed sell: " << profit << endl;
    }

    return profit;
}


double calcSharpeRatio(vector<double> opening_prices){
    double pf_returns = calcPortfolioReturn(opening_prices);
    double risk_free_rate = 0.05; // not specified in the question so i'm assuming this
    double std_dev = calcSD(opening_prices);
    return (pf_returns - risk_free_rate) / std_dev;
}

/**
 *  Driver code with test data
*/
int main(){
    //dummy data
    vector<double> opening_prices{20, 30, 25, 30, 25, 40, 35, 30, 35, 45, 50, 55, 50, 60, 70, 50, 55};
    cout << calcSharpeRatio(opening_prices) << endl;
}
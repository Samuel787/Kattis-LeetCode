'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
TC = input()

for i in range(int(TC)):
    prices = input().split()
    num = input()
    
    ### I'm finding all the indices of the peaks in the data
    peaks = []
    curr_peak = 0
    for index in range(len(prices)):
        if index == len(prices) - 1 and int(prices[index]) > int(curr_peak):
                peaks.append(index);
                curr_peak = prices[index];
        elif index != len(prices) - 1 and int(prices[index]) > int(prices[index + 1]) and int(prices[index]) > int(curr_peak):
                peaks.append(index);
                curr_peak = prices[index];

#     for i in peaks:
#         print(str(prices[i]) + " ")
    
    if len(peaks) < 2:
        print("None");
        continue;
    ### I'm finding all the troughs in the data

    ### trough is the minimum value between two peak indices
    counter = 0;
    results = [];
    while int(counter) < int(num):
        first_index = peaks[len(peaks) - counter - 1];
        second_index = peaks[len(peaks) - counter - 2];
        if (len(peaks) - counter - 2) < 0:
            break;
        
        ## find the trough in the window
        curr_trough = prices[second_index]
        for x in range(second_index + 1, first_index + 1):
            if int(prices[x]) < int(curr_trough):
                    curr_trough = int(prices[x]);
        
        results.append(int(prices[second_index]) - int(curr_trough));
        counter += 1

    print(*results);
#     for str(drawdown) in results:
#         print(str(drawdown) + " ");
    #print("end of tc")

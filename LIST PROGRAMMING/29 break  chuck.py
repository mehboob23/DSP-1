# Break a List into Chunks of Size N
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
chunk_size = int(input("Enter the size of each chunk: "))
chunks = [my_list[i:i+chunk_size] for i in range(0, len(my_list), chunk_size)]
print(f"List broken into chunks of size {chunk_size}:", chunks)

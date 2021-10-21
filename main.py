from tqdm import tdqm

LENGTH = 10 # Number of iterations required to fill pbar

pbar = tqdm(total=LENGTH) # Init pbar
for i in range(LENGTH):
  pbar.update(n=1) # Increments counter
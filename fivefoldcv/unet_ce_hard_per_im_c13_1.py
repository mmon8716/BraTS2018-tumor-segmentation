from subprocess import call

model = 'unet_ce_hard_per_im_c13'

#seeds = ['_s6916', '_s7435', '_s8841', '_s9527']

seeds = ['_s5713']

for seed in seeds:
	cfg_name = model+seed
	call(['python', 'train_unet.py', '--gpu', '2', '--cfg', cfg_name])
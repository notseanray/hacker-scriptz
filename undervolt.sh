sudo nvidia-smi -pm 1
sudo nvidia-smi -lgc 210,1860
sudo nvidia-settings -a "[gpu:0]/GPUGraphicsClockOffsetAllPerformanceLevels=210"

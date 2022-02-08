#!/bin/bash
for i in {1..40}
do
	wget https://whs-li.weebly.com/uploads/1/2/6/7/126780858/answer_to_ps_${i}.pdf
	echo "Downloaded ${i}"
done

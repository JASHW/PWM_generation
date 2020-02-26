module example(input wire clk,input wire [3:0] duty_cycle,output reg A);

reg[7:0] delay;

	always@(posedge clk) begin
	delay = delay+1;
	if(delay==100)
	 begin
        delay=0;
        end
        if(delay<(duty_cycle*10)) begin
	A=1;
	end
	else begin
	A=0;
	
	end
	end
endmodule

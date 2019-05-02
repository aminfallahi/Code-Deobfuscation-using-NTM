from Adafruit_PWM_Servo_Driver import PWM
class A:
	def __init__(A,i2cAddress,xAxisChannel,yAxisChannel,pwmFreqHz):A.pwm=PWM(i2cAddress,debug=True);A.pwm.setPWMFreq(pwmFreqHz);A.xaxis=xAxisChannel;A.yaxis=yAxisChannel
	def setXAxis(A,value):A.pwm.setPWM(A.xaxis,0,value)
	def setYAxis(A,value):A.pwm.setPWM(A.yaxis,0,value)
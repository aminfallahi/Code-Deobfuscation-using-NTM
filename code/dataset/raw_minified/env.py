class A:
	def create(A,isMaster):from tracker import MapOutputTracker as B;from fetch import SimpleShuffleFetcher as C;A.mapOutputTracker=B(isMaster);A.shuffleFetcher=C()
B=A()
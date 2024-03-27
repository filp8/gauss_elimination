import java.util.ArrayList;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Stream;

public class Matrix {
    
    public ArrayList<ArrayList<Integer>> core;
    private boolean scalarForm;

    public Matrix(ArrayList<Integer> firstLine) {
        core = new ArrayList<>();
        core.addLast(firstLine);
    }

    public void addLine(ArrayList<Integer> line) throws IndexOutOfBoundsException {
        int len = core.get(0).get(0);
        if (line.size() != len) {
            throw new IndexOutOfBoundsException("The line can be maximum long:" + len);
        }
        core.addLast(line);
    }

    public void toScalarForm() {
        //TODO: to finish this method
        int pivotIndex = 0;

        for(ArrayList<Integer> line : this.core) {
            int pivot = line.get(pivotIndex);
            if (pivot == 0) {
                if(
                    this.core.stream()
                                .skip(pivotIndex)
                                .anyMatch((nLine) -> nLine.get(0) != 0)
                ) {
                    AtomicInteger i_not_zero = new AtomicInteger(0);
                    this.core.stream()
                                .skip(pivotIndex + 1)
                                .allMatch((nLine) -> {
                                    i_not_zero.incrementAndGet();
                                    return nLine.get(pivotIndex) == 0;
                                });
                    this.switchLine(pivotIndex,i_not_zero.get());
                } else {
                    continue;
                }
            }
            this.simplify(pivotIndex,pivotIndex);

        }
        this.scalarForm = true;
    }

    private void simplify(int colon, int indexPivot) {
        int iteration = 0;
        Stream<ArrayList<Integer>> coreStream = this.core.stream()
                .skip(1);
        for(ArrayList<Integer> line : coreStream.toList()) {
            iteration++;
            if(this.core.get(indexPivot + iteration).get(colon) == 0)
                continue;
            // TODO: da finire questa funzione
            //ArrayList<Double> newLine = this.dotProduct(this.calculateScalar(line.get(indexPivot), iteration),line1,line2); 
        }

    }

    private void switchLine(int index1, int index2) {
        ArrayList<Integer> valueLine2 = this.core.get(index2);
        this.core.set(index2, this.core.get(index1));
        this.core.set(index1,valueLine2);
    }

    private double calculateScalar(float pivot,float a) {
        return (-1)*pivot*a;
    } 

    private ArrayList<Float> dotProduct(float scalar, ArrayList<Integer> line) {
        ArrayList<Float> result = new ArrayList<>();
        for(int e : line) {
            result.addLast(e * scalar);
        }

        return result;
    }

}

import org.junit.Test;
import static org.junit.Assert.*;

public class Day15Test {

    @Test
    public void testCalculateHash() {
        assertEquals( 200, Day15.calculateHash("H") );
        assertEquals( 153, Day15.calculateHash("HA") );
        assertEquals( 172, Day15.calculateHash("HAS") );
        assertEquals( 52,  Day15.calculateHash("HASH") );
        assertEquals( 0,   Day15.calculateHash("rn") );
        assertEquals( 1,   Day15.calculateHash("qp") );
        assertEquals( 30,  Day15.calculateHash("rn=1") );
    }

    @Test
    public void testTokenise() {
        String INPUT = """
                hello,

                world,every
                one
                """;
        String [] EXPECTED = new String[] {"hello","world","everyone"};       
        assertArrayEquals( EXPECTED, Day15.tokenise(INPUT) );
    }

    @Test
    public void testCalculateHashFullSequence() {
        assertEquals( 1320,   Day15.calculateHashFullSequence( TestData.SMALL_TEST ) );
        assertEquals( 507769, Day15.calculateHashFullSequence( TestData.FULL_TEST  ) ); // <<< PART1 answer!!
    }

    // /////////////////////////
    // PART2 functions...
    // 

    @Test
    public void testAddToBox() 
    {
        Day15.initBoxes();
        assertEquals( "", Day15.printBoxes().replace("\n","") );  

        // Add new entry to box 0
        Day15.addToBox("rn=1"); // box 0
        assertEquals( "Box[0] : [rn 1] ", Day15.printBoxes().replace("\n","") );        

        // Add new entry to box 1
        Day15.addToBox("qp=3"); // box 1
        assertEquals( "Box[0] : [rn 1] Box[1] : [qp 3] ", Day15.printBoxes().replace("\n","") );        

        // Add second entry to box 0
        Day15.addToBox("cm=5"); // box 0
        assertEquals( "Box[0] : [rn 1] [cm 5] Box[1] : [qp 3] ", Day15.printBoxes().replace("\n","") );  

        // Change the first entry in box 0
        Day15.addToBox("rn=999"); // box 0
        assertEquals( "Box[0] : [rn 999] [cm 5] Box[1] : [qp 3] ", Day15.printBoxes().replace("\n","") );          
    }

    @Test
    public void testRemoveFromBox() {
        Day15.initBoxes();
        assertEquals( "", Day15.printBoxes().replace("\n","") );  

        // Add new entry to box 0
        Day15.addToBox("rn=1"); // box 0     
        Day15.addToBox("cm=5"); // box 0
        Day15.addToBox("qp=3"); // box 1
        assertEquals( "Box[0] : [rn 1] [cm 5] Box[1] : [qp 3] ", Day15.printBoxes().replace("\n","") );  

        Day15.removeFromBox( "rn-");
        assertEquals( "Box[0] : [cm 5] Box[1] : [qp 3] ", Day15.printBoxes().replace("\n","") );  

        Day15.removeFromBox( "qp-");
        assertEquals( "Box[0] : [cm 5] ", Day15.printBoxes().replace("\n","") );  

        Day15.removeFromBox( "cm-");
        assertEquals( "", Day15.printBoxes().replace("\n","") );  
    }    

    @Test
    public void testPutLensesInBoxes() {

        // very short sequence
        Day15.initBoxes();    
        Day15.putLensesInBoxes("rn=1");      
        assertEquals( "Box[0] : [rn 1] ", Day15.printBoxes().replace("\n","") );        

        // the test sequence.
        String EXPECTED = "Box[0] : [rn 1] [cm 2] Box[3] : [ot 7] [ab 5] [pc 6] ";
        Day15.initBoxes();    
        Day15.putLensesInBoxes(TestData.SMALL_TEST);      
        assertEquals( EXPECTED, Day15.printBoxes().replace("\n","") );        
    }

    @Test
    public void testCalculateFocalPower() {
        Day15.initBoxes();    
        Day15.putLensesInBoxes("ot=7,rn=1,cm=2");      
        assertEquals( 33, Day15.calculateFocalPower( ) );           

        Day15.initBoxes();    
        Day15.putLensesInBoxes(TestData.SMALL_TEST);      
        assertEquals( 145, Day15.calculateFocalPower( ) );            

        Day15.initBoxes();    
        Day15.putLensesInBoxes(TestData.FULL_TEST);      
        assertEquals( 269747, Day15.calculateFocalPower( ) );       // <<< PART2 ANSWER!!        
    }

}

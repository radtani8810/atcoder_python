public class App {
    public static void main(String[] args) throws Exception {
        int dice =0;
        while(dice<6){
            dice = 1 + (int)(Math.random()*6.0);
            System.out.println("6以外が出ていないので継続");
        }
        System.out.println("6が出たので処理を終了します");
    }
}

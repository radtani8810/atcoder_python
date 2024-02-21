public class jihanki {
    public static void main(String[] args){
        int money =0;
        int total =0;

        for(int i = 0; i<(args.length)-1;i++){
            money = Integer.parseInt(args[i]);
            switch(money){
                case 1:
                    System.out.println("警告：1円玉は使えません");
                    break;
                case 5:
                    System.out.println("警告：5円玉は使えません");
                    break;
                case 10:
                    total+=money;
                    break;
                case 50:
                    total+=money;
                    break;
                case 100:
                    total+=money;
                    break;
                case 500:
                    total+=money;
                    break;
                default:
                    System.out.println("警告:"+money+"は硬貨として適切な値ではありません");
                    break;
            }
        }
        System.out.println((total- Integer.parseInt(args[args.length-1]))+"円のお釣りです。ありがとうございました。");
    }
}

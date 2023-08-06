
import paddle
from paddlenlp.transformers import BigBirdForPretraining, BigBirdTokenizer
from paddlenlp.transformers import create_bigbird_rand_mask_idx_list
paddle.set_device('cpu')
tokenizer = BigBirdTokenizer.from_pretrained('bigbird-base-uncased')
model = BigBirdForPretraining.from_pretrained('bigbird-base-uncased')
config = model.bigbird.config
max_seq_len = 512
input_ids, masked_lm_positions, masked_lm_ids, masked_lm_weights = tokenizer.encode(
        "This is a docudrama story on the Lindy Chamberlain case and a look at "
        "its impact on Australian society It especially looks at the problem of "
        "innuendo gossip and expectation when dealing with reallife dramasbr br "
        "One issue the story deals with is the way it is expected people will all "
        "give the same emotional response to similar situations Not everyone goes "
        "into wild melodramatic hysterics to every major crisis Just because the "
        "characters in the movies and on TV act in a certain way is no reason to "
        "expect real people to do so", max_seq_len=max_seq_len)

seq_len = len(input_ids)
input_ids = paddle.to_tensor([input_ids])
rand_mask_idx_list = create_bigbird_rand_mask_idx_list(
    config["num_layers"], seq_len, seq_len, config["nhead"],
    config["block_size"], config["window_size"], config["num_global_blocks"],
    config["num_rand_blocks"], config["seed"])
rand_mask_idx_list = [
    paddle.to_tensor(rand_mask_idx) for rand_mask_idx in rand_mask_idx_list
]
output = model(input_ids, rand_mask_idx_list=rand_mask_idx_list)
print(output[0].shape)
print(output[1].shape)

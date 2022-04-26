import math

def find_lr(trn_loader, optimizer, net, criterion, init_value = 1e-5, final_value=10., beta = 0.98):
    mult=1.2
    lr = init_value
    optimizer.param_groups[0]['lr'] = lr
    avg_loss = 0.
    batch_num = 0
    losses = []
    log_lrs = []
    lrs=[]

    for epoch in range(100):
        for item in trn_loader:
            batch_num+=1
            optimizer.zero_grad()
            out=net(item[0],item[1])
            loss=criterion(out,item[2].long())

            # Compute the smoothed loss
            avg_loss = beta * avg_loss + (1-beta) *loss.detach().item()
            smoothed_loss = avg_loss / (1 - beta**batch_num)

            losses.append(smoothed_loss)
            log_lrs.append(math.log10(lr))
            lrs.append(lr)

            # Do the step
            loss.backward()
            optimizer.step()

            # Update the lr for the next step
            lr *= mult
            optimizer.param_groups[0]['lr'] = lr      

            if lrs[-1]>1:
                return log_lrs,lrs,losses

    return log_lrs,lrs, losses
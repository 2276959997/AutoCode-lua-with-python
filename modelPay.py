# coding:utf8
modelPayList = ['<packageName>', '<ClassName>']
modelPay = """
package <packageName>;

import java.util.UUID;
import android.R.string;
import android.app.Activity;
import com.ansca.corona.CoronaEnvironment;
import com.naef.jnlua.LuaState;
import com.naef.jnlua.LuaType;
import com.naef.jnlua.NamedJavaFunction;

public class <ClassName> implements NamedJavaFunction{

	private LuaState lua;
	@Override
	public int invoke(LuaState luaState) {

		this.lua = luaState;
		final String serverName = luaState.checkString(1);
		final float amount = (float)luaState.checkNumber(2);
		final String productName = luaState.checkString(3);
		final String roleName = luaState.checkString(4);
		final String roleId = luaState.checkString(5);
		final String severId = luaState.checkString(6);
		final String cusInfo = luaState.checkString(7);
		int functionIndex = 8;
		luaState.checkType(functionIndex, LuaType.FUNCTION);
		luaState.pushValue(functionIndex);
		final int registryIndex = luaState.ref(LuaState.REGISTRYINDEX);

		CoronaEnvironment.getCoronaActivity().runOnUiThread(new Runnable() {
			@Override
			public void run() {
				Activity ctx = CoronaEnvironment.getCoronaActivity();
				String orderId = UUID.randomUUID().toString().replace("-", "");

				downjoy.openPaymentDialog(ctx, amount, productName, productName, orderId, info, severId, serverName, roleId, roleName, new CallbackListener<String>() {

					@Override
					public void callback(int status, String orderId) {
						if (status == CallbackStatus.SUCCESS){
							lua.rawGet(LuaState.REGISTRYINDEX, registryIndex);
							lua.unref(LuaState.REGISTRYINDEX, registryIndex);

							lua.newTable(0, 3);
							int tableIndex = lua.getTop();
							lua.pushInteger(0);
							lua.setField(tableIndex, "statusCode");
							lua.pushNumber(Double.valueOf(amount));
							lua.setField(tableIndex, "amount");
							lua.pushString(orderId);
							lua.setField(tableIndex, "orderId");
							lua.call(1, 0);
						}else if (status == CallbackStatus.FAIL){
							lua.rawGet(LuaState.REGISTRYINDEX, registryIndex);
							lua.unref(LuaState.REGISTRYINDEX, registryIndex);

							lua.newTable(0, 3);
							int tableIndex = lua.getTop();
							lua.pushInteger(1);
							lua.setField(tableIndex, "statusCode");
							lua.pushNumber(Double.valueOf(amount));
							lua.setField(tableIndex, "amount");
							lua.pushString(orderId);
							lua.setField(tableIndex, "orderId");
							lua.call(1, 0);
						}

					}
				});
			}
		});
		return 0;
	}

	@Override
	public String getName() {
		return "pay";
	}

}
"""
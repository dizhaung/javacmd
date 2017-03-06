package com.yp.test.comm;

import org.apache.log4j.ConsoleAppender;
import org.apache.log4j.Layout;
import org.apache.log4j.Logger;
import org.apache.log4j.PatternLayout;
import org.apache.log4j.RollingFileAppender;

public class LogCommon2 {

	/**
	 * 把日志路径给填充好
	 * 
	 * @param currentBusiCode
	 * @param taskLog
	 * @param errLogger
	 */
	public static void fillLogger(String currentBusiCode, Logger taskLog) {
		try {
			String foldPath = "D:/";
			Layout layout = new PatternLayout("%d %p [%c][%t] - %m%n");
			
			//定义日志路径
			String taskLogPath = foldPath +  "/stalog/"+ currentBusiCode + ".log";
			
			//定两个   fileAppender,用于输出日志
			RollingFileAppender taskAppender = new RollingFileAppender(layout, taskLogPath);
			taskAppender.setMaxFileSize("1MB");
			taskAppender.setMaxBackupIndex(10);
			taskAppender.setName("fa");
			
			//已经存在了，就不处理了,
			if(taskLog.getAppender("fa")==null){
				taskLog.addAppender(taskAppender);
				ConsoleAppender c = new ConsoleAppender();
				c.setLayout(layout);
				taskLog.addAppender(c);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
